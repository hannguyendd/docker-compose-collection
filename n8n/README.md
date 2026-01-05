# N8N Workflow Automation with Docker Compose

This repository contains a Docker Compose setup for running N8N (workflow automation tool) with a dedicated PostgreSQL database.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository
2. Run the following command:

```bash
docker compose -f n8n/n8n.yaml -p n8n up -d
```

## Configuration

The following environment variables can be configured in a `.env` file:

- `HOST_PORT`: The host port for N8N web interface (default: 5678)
- `POSTGRES_PORT`: The host port for PostgreSQL (default: 5433)
- `POSTGRES_USER`: Database user (default: n8n)
- `POSTGRES_PASSWORD`: Database password (default: n8npassword)
- `POSTGRES_DB`: Database name (default: n8n)

Example `.env` file:

```env
HOST_PORT=5678
POSTGRES_PORT=5433
POSTGRES_USER=n8n
POSTGRES_PASSWORD=secure_password
POSTGRES_DB=n8n
```

## Connection Details

### N8N Web Interface

- **URL**: http://localhost:5678 (default)
- **First time setup**: Create your admin account on first access

### PostgreSQL Database

- **Host**: localhost
- **Port**: 5433 (default, to avoid conflict with other PostgreSQL instances)
- **Username**: n8n (default)
- **Password**: n8npassword (default)
- **Database**: n8n (default)

## Persistence

Data is persisted using Docker volumes:

- `n8n_data`: N8N workflows and configuration
- `n8n_postgres_data`: PostgreSQL database data

## Container Management

Start the containers:

```bash
docker compose -f n8n/n8n.yaml -p n8n up -d
```

Stop the containers:

```bash
docker compose -f n8n/n8n.yaml -p n8n down
```

View logs:

```bash
docker compose -f n8n/n8n.yaml -p n8n logs -f
```

Remove containers and volumes (⚠️ deletes all data):

```bash
docker compose -f n8n/n8n.yaml -p n8n down -v
```

## Notes

- N8N uses PostgreSQL as its database backend for better performance and reliability
- The PostgreSQL database is exposed on port 5433 (default) to avoid conflicts with other PostgreSQL instances
- Health checks ensure PostgreSQL is ready before N8N starts
- Both services have `restart: always` policy for automatic recovery

## License

MIT License
