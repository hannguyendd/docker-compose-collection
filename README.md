# Docker Compose Collection

A collection of Docker Compose configurations for various applications and services.

## Available Configurations

### LocalStack

Fully functional local AWS cloud stack for developing and testing cloud & serverless applications offline.
[View Details](localstack/README.md)

### N8N Workflow Automation

N8N workflow automation platform with PostgreSQL database.
[View Details](n8n/README.md)

### Ollama Chat UI

Web interface for interacting with Ollama language models.
[View Details](ollama-chat-ui/README.md)

### PostgreSQL Database

PostgreSQL database instance with configurable settings.
[View Details](postgres-db/README.md)

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
├── localstack/
│   ├── localstack.yaml
│   └── README.md
├── n8n/
│   ├── n8n.yaml
│   └── README.md
├── ollama-chat-ui/
│   ├── ollama-chat-ui.yaml
│   └── README.md
└── postgres-db/
    ├── postgres-db.yaml
    └── README.md
```

## Contributing

Feel free to contribute by adding new Docker Compose configurations or improving existing ones.

## License

MIT License
