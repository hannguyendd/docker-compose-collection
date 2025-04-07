# Ollama Chat UI with Docker Compose

This repository contains a Docker Compose setup for running Ollama Chat UI, a web interface for interacting with Ollama language models.

## Prerequisites

- Docker
- Docker Compose
- Ollama

## Quick Start

1. Clone this repository
2. Run the following command:

```bash
docker compose -f ollama-chat-ui/ollama-chat-ui.yaml -p ollama-chat-ui up
```

## Services

- **Ollama Server**: Runs the Ollama language model service
- **Chat UI**: Web interface for interacting with Ollama

## Usage

1. Access the Chat UI at `http://localhost:8801`
2. The Ollama server runs at `http://localhost:11434`

## Configuration

Modify the `docker-compose.yml` file to adjust service configurations as needed.

## License

MIT License
