# OpenSearch

[OpenSearch](https://opensearch.org/) is a community-driven, open-source search and analytics suite derived from Elasticsearch. This setup includes OpenSearch and OpenSearch Dashboards.

## Quick Start

```bash
# Start the service
./run-service.sh opensearch

# View logs
./run-service.sh opensearch logs -f

# Stop the service
./run-service.sh opensearch down

# Stop and remove volumes
./run-service.sh opensearch down -v
```

## Ports

| Service | Port | Description |
|---------|------|-------------|
| OpenSearch | 9200 | REST API |
| OpenSearch | 9600 | Performance Analyzer |
| OpenSearch Dashboards | 5601 | Web UI |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENSEARCH_PORT` | `9200` | Host port for OpenSearch REST API |
| `OPENSEARCH_PERF_PORT` | `9600` | Host port for Performance Analyzer |
| `OPENSEARCH_INITIAL_ADMIN_PASSWORD` | `MyStr0ng!Pass` | Admin password (must meet complexity requirements) |
| `OPENSEARCH_JAVA_OPTS` | `-Xms512m -Xmx512m` | JVM heap size |
| `DISABLE_SECURITY_PLUGIN` | `false` | Disable security plugin (set to `true` for dev) |
| `OPENSEARCH_DASHBOARDS_PORT` | `5601` | Host port for Dashboards UI |
| `DISABLE_SECURITY_DASHBOARDS_PLUGIN` | `false` | Disable Dashboards security plugin |

## Connection Details

### With Security Enabled (default)

```
URL: https://localhost:9200
Username: admin
Password: MyStr0ng!Pass (or your configured password)
```

### With Security Disabled

Set `DISABLE_SECURITY_PLUGIN=true` and `DISABLE_SECURITY_DASHBOARDS_PLUGIN=true`:

```
URL: http://localhost:9200
```

### Dashboards

```
URL: http://localhost:5601
```

## Verify

```bash
# Check cluster health (with security enabled)
curl -ku admin:MyStr0ng!Pass https://localhost:9200/_cluster/health?pretty

# Check cluster health (with security disabled)
curl http://localhost:9200/_cluster/health?pretty
```

## Dashboards Features

The following features are enabled by default in this setup:

| Setting | Description |
|---------|-------------|
| `data_source.enabled` | **Multi-cluster support** — Connect to multiple OpenSearch clusters from a single Dashboards instance. Useful for managing dev/staging/prod from one UI. |
| `workspace.enabled` | **Workspaces** — Isolated spaces for teams or projects. Each workspace gets its own dashboards, visualizations, and index patterns without interfering with others. |
| `explore.enabled` | **Explore UI** — Enhanced log exploration interface for browsing and querying data, similar to Kibana Discover but with improved UX. |

## Notes

- The `vm.max_map_count` kernel setting should be at least 262144 for production use. On macOS with Docker Desktop, this is handled automatically.
- The admin password must meet OpenSearch complexity requirements: at least 8 characters, including uppercase, lowercase, digit, and special character.
