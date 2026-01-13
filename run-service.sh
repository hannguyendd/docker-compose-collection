#!/bin/bash

# Docker Compose Collection - Service Runner
# Usage: ./run-service.sh <service-name> [action]
# Example: ./run-service.sh postgres-db up -d

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Available services
SERVICES=(
    "influxdb3"
    "localstack"
    "milvus"
    "n8n"
    "ollama-chat-ui"
    "postgres-db"
)

# Function to display usage
show_usage() {
    echo -e "${BLUE}Docker Compose Collection - Service Runner${NC}"
    echo ""
    echo "Usage: $0 <service-name> [action]"
    echo ""
    echo -e "${YELLOW}Available services:${NC}"
    for service in "${SERVICES[@]}"; do
        echo "  - $service"
    done
    echo ""
    echo -e "${YELLOW}Common actions:${NC}"
    echo "  up -d       - Start service in detached mode (default)"
    echo "  up          - Start service and show logs"
    echo "  down        - Stop and remove containers"
    echo "  down -v     - Stop and remove containers and volumes"
    echo "  logs        - View logs"
    echo "  logs -f     - Follow logs"
    echo "  ps          - List containers"
    echo "  restart     - Restart service"
    echo "  stop        - Stop service"
    echo "  start       - Start existing service"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 postgres-db up -d"
    echo "  $0 n8n logs -f"
    echo "  $0 localstack down"
}

# Function to check if service exists
service_exists() {
    local service=$1
    for s in "${SERVICES[@]}"; do
        if [ "$s" = "$service" ]; then
            return 0
        fi
    done
    return 1
}

# Function to get compose file path
get_compose_file() {
    local service=$1
    
    # Special case for milvus
    if [ "$service" = "milvus" ]; then
        echo "$service/standalone.yml"
    else
        echo "$service/$service.yaml"
    fi
}

# Main logic
if [ $# -eq 0 ]; then
    show_usage
    exit 1
fi

SERVICE_NAME=$1
shift  # Remove first argument, keep the rest as action

# Default action if none provided
if [ $# -eq 0 ]; then
    ACTION="up -d"
else
    ACTION="$@"
fi

# Validate service name
if ! service_exists "$SERVICE_NAME"; then
    echo -e "${RED}Error: Unknown service '$SERVICE_NAME'${NC}"
    echo ""
    show_usage
    exit 1
fi

# Get compose file path
COMPOSE_FILE=$(get_compose_file "$SERVICE_NAME")

# Check if compose file exists
if [ ! -f "$COMPOSE_FILE" ]; then
    echo -e "${RED}Error: Compose file not found: $COMPOSE_FILE${NC}"
    exit 1
fi

# Execute docker compose command
echo -e "${GREEN}Running: docker compose -f $COMPOSE_FILE -p $SERVICE_NAME $ACTION${NC}"
echo ""

docker compose -f "$COMPOSE_FILE" -p "$SERVICE_NAME" $ACTION

echo ""
echo -e "${GREEN}✓ Command executed successfully${NC}"

# Show helpful message based on action
if [[ "$ACTION" == "up"* ]]; then
    echo ""
    echo -e "${BLUE}Service '$SERVICE_NAME' is starting...${NC}"
    echo -e "View logs: ${YELLOW}./run-service.sh $SERVICE_NAME logs -f${NC}"
    echo -e "Stop service: ${YELLOW}./run-service.sh $SERVICE_NAME down${NC}"
fi
