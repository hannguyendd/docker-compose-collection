# InfluxDB 3 with UI

InfluxDB 3 Core time-series database with the official InfluxDB 3 UI for exploration.

## Quick Start

```bash
# Using the service runner
./run-service.sh influxdb3

# Or directly with docker compose
docker compose -f influxdb3/influxdb3.yaml -p influxdb3 up -d
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| InfluxDB 3 | 8181 | Time-series database (HTTP API) |
| InfluxDB 3 UI | 8282 | Database explorer and query interface |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `INFLUXDB_PORT` | 8181 | InfluxDB HTTP API port |
| `INFLUXDB3_NODE_ID` | node0 | Node identifier for InfluxDB |
| `INFLUXDB_UI_PORT` | 8282 | InfluxDB 3 UI port |

## Access

- **InfluxDB 3 UI**: http://localhost:8282
- **InfluxDB API**: http://localhost:8181

## Usage

### Create a Database

```bash
curl -X POST "http://localhost:8181/api/v3/configure/database" \
  -H "Content-Type: application/json" \
  -d '{"name": "mydb"}'
```

### Write Data (Line Protocol)

```bash
curl -X POST "http://localhost:8181/api/v3/write_lp?db=mydb" \
  -H "Content-Type: text/plain" \
  -d 'cpu,host=server01 usage=0.64'
```

### Query Data (SQL)

```bash
curl -X POST "http://localhost:8181/api/v3/query_sql" \
  -H "Content-Type: application/json" \
  -d '{"db": "mydb", "q": "SELECT * FROM cpu"}'
```

## Volumes

| Volume | Purpose |
|--------|---------|
| `influxdb3_data` | InfluxDB data persistence |

## Stopping the Service

```bash
# Stop containers
./run-service.sh influxdb3 down

# Stop and remove volumes
./run-service.sh influxdb3 down -v
```
