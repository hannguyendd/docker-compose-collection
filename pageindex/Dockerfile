FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*

# Clone PageIndex repository and install dependencies
RUN git clone https://github.com/VectifyAI/PageIndex.git /app/pageindex-repo && \
    pip install --no-cache-dir -r /app/pageindex-repo/requirements.txt && \
    pip install --no-cache-dir fastapi uvicorn python-multipart

# Copy the API server
COPY server.py /app/server.py

# Create directories for data and documents
RUN mkdir -p /app/data /app/documents

EXPOSE 8090

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8090"]
