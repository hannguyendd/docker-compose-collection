# Docker Compose Collection

A collection of Docker Compose configurations for various applications and services.

## Quick Start

Use the provided script to easily manage services:

```bash
./run-service.sh <service-name> [action]
```

Examples:

```bash
# Start a service (detached mode by default)
./run-service.sh postgres-db
./run-service.sh n8n up -d

# View logs
./run-service.sh localstack logs -f

# Stop a service
./run-service.sh ollama-chat-ui down

# Stop and remove volumes
./run-service.sh postgres-db down -v
```

Run without arguments to see all available services and actions:

```bash
./run-service.sh
```

## Available Configurations

### InfluxDB 3

InfluxDB 3 Core time-series database with official UI for exploration.
[View Details](influxdb3/README.md)

### LocalStack

Fully functional local AWS cloud stack for developing and testing cloud & serverless applications offline.
[View Details](localstack/README.md)

### N8N Workflow Automation

N8N workflow automation platform with PostgreSQL database.
[View Details](n8n/README.md)

### Ollama Chat UI

Web interface for interacting with Ollama language models.
[View Details](ollama-chat-ui/README.md)

### OpenSearch

OpenSearch search and analytics suite with OpenSearch Dashboards.
[View Details](opensearch/README.md)

### PageIndex for RAG

Vectorless, reasoning-based RAG service using PageIndex. Transforms documents into tree-structured indexes for LLM retrieval without vector databases.
[View Details](pageindex/README.md)

### PostgreSQL Database

PostgreSQL database instance with configurable settings.
[View Details](postgres-db/README.md)

### Redis Stack

Redis with built-in modules (RedisSearch, RedisJSON, RedisGraph, RedisTimeSeries, RedisBloom) and RedisInsight UI.
[View Details](redis/README.md)

## Usage

Each service has its own directory containing:

- A Docker Compose YAML file
- A README with specific setup instructions
- Any additional configuration files

To run a service:

```bash
docker compose -f <service-directory>/<compose-file>.yaml -p <project-name> up
```

Examples:

```bash
docker compose -f localstack/localstack.yaml -p localstack up -d
docker compose -f n8n/n8n.yaml -p n8n up -d
docker compose -f ollama-chat-ui/ollama-chat-ui.yaml -p ollama-chat-ui up
```

## Structure

```
.
├── .gitignore
├── README.md
├── influxdb3/
│   ├── influxdb3.yaml
│   └── README.md
├── localstack/
│   ├── localstack.yaml
│   └── README.md
├── n8n/
│   ├── n8n.yaml
│   └── README.md
├── ollama-chat-ui/
│   ├── ollama-chat-ui.yaml
│   └── README.md
├── opensearch/
│   ├── opensearch.yaml
│   └── README.md
├── pageindex/
│   ├── pageindex.yaml
│   ├── Dockerfile
│   ├── server.py
│   └── README.md
├── postgres-db/
│   ├── postgres-db.yaml
│   └── README.md
└── redis/
    ├── redis.yaml
    └── README.md
```

## Contributing

Feel free to contribute by adding new Docker Compose configurations or improving existing ones.

## License

MIT License
