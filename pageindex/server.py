"""Lightweight FastAPI wrapper around PageIndex for document indexing and RAG."""

import json
import os
import subprocess
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="PageIndex API", description="Vectorless reasoning-based RAG service")

DOCUMENTS_DIR = Path("/app/documents")
DATA_DIR = Path("/app/data")
PAGEINDEX_SCRIPT = Path("/app/pageindex-repo/run_pageindex.py")


class IndexRequest(BaseModel):
    filename: str
    model: str | None = None
    toc_check_pages: int | None = None
    max_pages_per_node: int | None = None
    max_tokens_per_node: int | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/documents")
def list_documents():
    """List all uploaded documents."""
    files = []
    for f in DOCUMENTS_DIR.iterdir():
        if f.is_file():
            files.append({"name": f.name, "size": f.stat().st_size})
    return {"documents": files}


@app.get("/indexes")
def list_indexes():
    """List all generated indexes."""
    files = []
    for f in DATA_DIR.iterdir():
        if f.is_file():
            files.append({"name": f.name, "size": f.stat().st_size})
    return {"indexes": files}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF or Markdown document."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    suffix = Path(file.filename).suffix.lower()
    if suffix not in (".pdf", ".md"):
        raise HTTPException(status_code=400, detail="Only .pdf and .md files are supported")

    dest = DOCUMENTS_DIR / file.filename
    content = await file.read()
    dest.write_bytes(content)
    return {"message": f"Uploaded {file.filename}", "size": len(content)}


@app.post("/index")
def create_index(request: IndexRequest):
    """Run PageIndex on an uploaded document to generate a tree index."""
    doc_path = DOCUMENTS_DIR / request.filename
    if not doc_path.exists():
        raise HTTPException(status_code=404, detail=f"Document not found: {request.filename}")

    suffix = doc_path.suffix.lower()
    if suffix == ".pdf":
        path_flag = "--pdf_path"
    elif suffix == ".md":
        path_flag = "--md_path"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    model = request.model or os.environ.get("PAGEINDEX_MODEL", "gpt-4o")
    toc_pages = request.toc_check_pages or int(os.environ.get("PAGEINDEX_TOC_CHECK_PAGES", "20"))
    max_pages = request.max_pages_per_node or int(os.environ.get("PAGEINDEX_MAX_PAGES_PER_NODE", "10"))
    max_tokens = request.max_tokens_per_node or int(os.environ.get("PAGEINDEX_MAX_TOKENS_PER_NODE", "20000"))

    cmd = [
        sys.executable, str(PAGEINDEX_SCRIPT),
        path_flag, str(doc_path),
        "--model", model,
        "--toc-check-pages", str(toc_pages),
        "--max-pages-per-node", str(max_pages),
        "--max-tokens-per-node", str(max_tokens),
    ]

    env = {**os.environ}

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=600)
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Indexing timed out (10 min limit)")

    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {result.stderr}")

    # Move any generated output to data directory
    output_files = []
    for f in Path("/app/pageindex-repo").glob("*.json"):
        dest = DATA_DIR / f.name
        f.rename(dest)
        output_files.append(dest.name)

    return {
        "message": "Indexing complete",
        "output_files": output_files,
        "stdout": result.stdout[-2000:] if result.stdout else "",
    }


@app.get("/indexes/{filename}")
def get_index(filename: str):
    """Retrieve a generated index file."""
    index_path = DATA_DIR / filename
    if not index_path.exists():
        raise HTTPException(status_code=404, detail=f"Index not found: {filename}")

    try:
        return json.loads(index_path.read_text())
    except json.JSONDecodeError:
        return {"content": index_path.read_text()}
