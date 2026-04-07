# PageIndex for RAG

Vectorless, reasoning-based RAG service using [PageIndex](https://github.com/VectifyAI/PageIndex). Transforms documents into tree-structured indexes for LLM-based retrieval without vector databases.

## Quick Start

```bash
# Copy and configure environment variables
cp .env.example .env
# Edit .env and set your CHATGPT_API_KEY

# Start the service
../../run-service.sh pageindex
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `CHATGPT_API_KEY` | (required) | OpenAI API key |
| `PAGEINDEX_PORT` | `8090` | Host port for the API |
| `PAGEINDEX_MODEL` | `gpt-4o` | OpenAI model for indexing |
| `PAGEINDEX_TOC_CHECK_PAGES` | `20` | Pages to scan for TOC |
| `PAGEINDEX_MAX_PAGES_PER_NODE` | `10` | Max pages per tree node |
| `PAGEINDEX_MAX_TOKENS_PER_NODE` | `20000` | Max tokens per tree node |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/documents` | List uploaded documents |
| `GET` | `/indexes` | List generated indexes |
| `POST` | `/upload` | Upload a PDF or Markdown file |
| `POST` | `/index` | Run PageIndex on a document |
| `GET` | `/indexes/{filename}` | Retrieve a generated index |

## Usage

### Upload a document

```bash
curl -X POST http://localhost:8090/upload \
  -F "file=@/path/to/document.pdf"
```

### Create an index

```bash
curl -X POST http://localhost:8090/index \
  -H "Content-Type: application/json" \
  -d '{"filename": "document.pdf"}'
```

### Retrieve the index

```bash
curl http://localhost:8090/indexes
curl http://localhost:8090/indexes/document_index.json
```

### Interactive API docs

Visit [http://localhost:8090/docs](http://localhost:8090/docs) for the Swagger UI.

## Volumes

| Volume | Purpose |
|--------|---------|
| `pageindex_data` | Persisted generated indexes |
| `./documents` | Local directory for document input |

## Stopping the Service

```bash
../../run-service.sh pageindex down

# Remove volumes
../../run-service.sh pageindex down -v
```
