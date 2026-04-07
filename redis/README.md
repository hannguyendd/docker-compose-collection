# Redis Stack

Redis Stack includes Redis with RedisSearch, RedisJSON, RedisGraph, RedisTimeSeries, and RedisBloom modules, plus RedisInsight for management.

## Quick Start

```bash
./run-service.sh redis
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `REDIS_PORT` | `6379` | Redis server port |
| `REDIS_INSIGHT_PORT` | `8001` | RedisInsight web UI port |
| `REDIS_ARGS` | `--requirepass password` | Redis server arguments |

## Connection Details

- **Redis**: `localhost:6379`
- **RedisInsight UI**: http://localhost:8001
- **Default password**: `password`

### CLI Connection

```bash
redis-cli -h localhost -p 6379 -a password
```

## Stopping

```bash
./run-service.sh redis down

# Remove data volumes
./run-service.sh redis down -v
```
