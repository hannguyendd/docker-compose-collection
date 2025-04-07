# PostgreSQL Database with Docker Compose

This repository contains a Docker Compose setup for running a PostgreSQL database instance.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository
2. Run the following command:

```bash
docker compose -f postgres-db/postgres-db.yaml -p postgres-db up -d
```

## Configuration

The following environment variables can be configured in a `.env` file:

- `HOST_PORT`: The host port to bind (default: 5432)
- `POSTGRES_USER`: Database user (default: postgres)
- `POSTGRES_PASSWORD`: Database password (default: password)

Example `.env` file:

```env
HOST_PORT=5432
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```

## Connection Details

- **Host**: localhost
- **Port**: 5432 (default)
- **Username**: postgres (default)
- **Password**: password (default)
- **Database**: postgres (default)

## Persistence

Data is persisted using a Docker volume named `postgres-db-for-optimization-course`.

## Container Management

Start the container:
```bash
docker compose up -d
```

Stop the container:
```bash
docker compose down
```

View logs:
```bash
docker compose logs -f
```

## License

MIT License