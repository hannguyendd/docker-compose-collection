# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A curated collection of Docker Compose configurations for common development services. Each service is self-contained in its own directory with a compose file and README.

## Commands

### Service Management

Use the convenience script for all service operations:

```bash
./run-service.sh <service-name> [action]
```

Common actions:
- `./run-service.sh postgres-db` - Start service (detached mode default)
- `./run-service.sh n8n logs -f` - Follow logs
- `./run-service.sh localstack down` - Stop service
- `./run-service.sh milvus down -v` - Stop and remove volumes

Without arguments shows available services and actions.

### Direct Docker Compose

```bash
docker compose -f <service>/<service>.yaml -p <service> up -d
docker compose -f <path> config  # Validate syntax
```

## Architecture

### Directory Structure Pattern

```
<service-name>/
├── <service-name>.yaml    # Docker Compose configuration
└── README.md              # Service-specific documentation
```

Exception: Milvus uses `standalone.yml` instead of `.yaml`.

### Available Services

| Service | Port | Notes |
|---------|------|-------|
| influxdb3 | 8181, 8282, 8283 | InfluxDB 3 time-series DB with Explorer UI (admin mode) |
| localstack | 4566 | Local AWS cloud stack |
| milvus | 19530 | Vector database (multi-container: etcd, MinIO, Milvus) |
| n8n | 5678 | Workflow automation with PostgreSQL backend (postgres on 5433) |
| ollama-chat-ui | 8801 | Open WebUI for Ollama (requires host Ollama) |
| postgres-db | 5432 | PostgreSQL instance |

## Conventions

### File Naming
- Compose files use `.yaml` extension (except Milvus: `standalone.yml`)
- Compose file matches directory name: `postgres-db/postgres-db.yaml`

### Environment Variables
- All `.env` files are gitignored
- Use `${VARIABLE:-default}` pattern for defaults
- Port pattern: `${HOST_PORT:-default}:container_port`

### Volume Naming
- Pattern: `<service>_<purpose>` (e.g., `postgres_db_data`, `n8n_data`)

## Adding New Services

1. Create directory: lowercase, hyphenated name
2. Create `<service-name>.yaml` with:
   - Named volumes for persistence
   - Environment defaults via `${VAR:-default}`
   - Configurable ports via `${HOST_PORT:-default}`
3. Create `README.md` with quick start, env vars, connection details
4. Update root `README.md` with new service
5. Add service to `SERVICES` array in `run-service.sh`
