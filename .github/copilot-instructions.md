# Docker Compose Collection - AI Agent Instructions

## Project Architecture

This is a **curated collection of Docker Compose configurations** for deploying common development services. Each service is self-contained in its own directory with a compose file and dedicated README.

### Structure Pattern

```
<service-name>/
├── <service-name>.yaml    # Docker Compose configuration
└── README.md             # Service-specific documentation
```

Current services:

- **localstack/**: Fully functional local AWS cloud stack (port 4566)
- **milvus/**: Vector database with etcd, MinIO, and Milvus standalone (port 19530)
- **n8n/**: Workflow automation platform with PostgreSQL backend (port 5678)
- **ollama-chat-ui/**: Open WebUI for Ollama models (port 8801)
- **postgres-db/**: PostgreSQL instance with persistent volume

## Key Conventions

### File Naming

- Compose files use `.yaml` extension (not `.yml`), except Milvus which uses `standalone.yml`
- Compose files are named after their service directory (e.g., `postgres-db/postgres-db.yaml`)
- Each service has its own README.md explaining configuration and usage

### Project Naming

Run services using the `-p` flag with project name matching the directory:

```bash
docker compose -f <service>/<service>.yaml -p <service> up
```

Example: `docker compose -f postgres-db/postgres-db.yaml -p postgres-db up -d`

### Environment Configuration

- All `.env` files are gitignored
- Services use `${VARIABLE:-default}` pattern for environment variables
- Common pattern: `HOST_PORT` for customizable port mapping (e.g., `${HOST_PORT:-5432}:5432`)
- Default credentials should be documented in each service's README

### Volume Management

- Each service uses named volumes for persistence
- Volume names follow pattern: `<service>_<purpose>` or descriptive names
- Examples: `postgres_db_data`, `open-webui`, `volumes/milvus`

## Adding New Services

When adding a new service:

1. Create directory named after the service (lowercase, hyphenated)
2. Create `<service-name>.yaml` with:
   - Named service containers
   - Environment variable defaults using `${VAR:-default}` syntax
   - Named volumes for persistence
   - Exposed ports via `${HOST_PORT:-default}` when user-configurable
3. Create `README.md` with:
   - Quick start command
   - Environment variable documentation
   - Connection details and default credentials
   - Container management commands
4. Update root [README.md](../README.md) with new service entry and example

## Service-Specific Notes

### LocalStack

- Single-container AWS cloud emulator
- Supports wide range of AWS services (S3, DynamoDB, Lambda, SQS, SNS, etc.)
- Uses `HOST_PORT` for gateway (default 4566) and `HOST_PORT_INTERNAL` for internal services (4510-4559)
- Default AWS credentials: `test`/`test`
- Volume: `localstack_data`

### Milvus

- Multi-container setup (etcd, MinIO, Milvus)
- Uses custom network named "milvus"
- Supports `DOCKER_VOLUME_DIRECTORY` for custom volume paths
- Health checks configured for all containers

### N8N

- Multi-container setup (PostgreSQL + N8N)
- PostgreSQL exposed on port 5433 (default) to avoid conflicts
- Health check ensures PostgreSQL is ready before N8N starts
- Volumes: `n8n_data` and `n8n_postgres_data`
- Default database credentials: `n8n`/`n8npassword`

### Ollama Chat UI

- Requires host Ollama installation or separate Ollama container
- Uses `host.docker.internal:host-gateway` to connect to host services
- Based on Open WebUI (ghcr.io/open-webui/open-webui:main)

### PostgreSQL

- Volume name is project-specific: `postgres-db-for-optimization-course`
- Always uses `restart: always` policy

## Testing Changes

Test compose files with:

```bash
docker compose -f <path> config          # Validate syntax
docker compose -f <path> -p test up -d   # Start detached
docker compose -f <path> -p test down    # Clean up
```
