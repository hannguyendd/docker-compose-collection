# Docker Compose Collection

A collection of Docker Compose configurations for various applications and services.

## Available Configurations

### Ollama Chat UI

Web interface for interacting with Ollama language models.
[View Details](ollama-chat-ui/README.md)

## Usage

Each service has its own directory containing:

- A Docker Compose YAML file
- A README with specific setup instructions
- Any additional configuration files

To run a service:

```bash
docker compose -f <service-directory>/<compose-file>.yaml -p <project-name> up
```

Example:

```bash
docker compose -f ollama-chat-ui/ollama-chat-ui.yaml -p ollama-chat-ui up
```

## Structure

```
.
├── .gitignore
├── README.md
└── ollama-chat-ui/
    ├── ollama-chat-ui.yaml
    └── README.md
```

## Contributing

Feel free to contribute by adding new Docker Compose configurations or improving existing ones.

## License

MIT License
