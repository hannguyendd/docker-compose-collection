---
name: init-docker-compose
description: Set up and manage local development services using Docker Compose with a standardized directory structure and convenience scripts.
disable-model-invocation: true
user-invokable: true
---

# Docker Compose Initializer

## This skill helps you set up docker compose file to run service $ARGUMENTS locally.

# Process

## Create a directory for the service

create a directory named after the service you want to run. For example, if you want to run a PostgreSQL database, create a directory called `postgres-db`.

folder structure:

```
<service-name>/
├── docker-compose.yml
├── .env.example (optional)
├── README.md
└── .env (gitignored)
```

## Create a docker-compose.yml file

Inside the service directory, create a `docker-compose.yml` file that defines the service configuration.

- DON'T need to specify the version in the compose file.
- Use the NEWEST version of docker compose syntax (without version field).
- Use the NEWEST version of the image for the service.
- Mount any necessary volumes for data persistence or configuration.
- Expose the necessary ports for the service.
- Define any necessary environment variables in the compose file or in a separate `.env` file.

## Create a .env file (optional)

If your service requires environment variables, create a `.env` file in the service directory to store them.

## Create a .env.example file (optional)

If you have a `.env` file, create a `.env.example` file that contains the same environment variable keys but with placeholder values. This file can be committed to version control to provide a reference for the required environment variables without exposing sensitive information.

## Update run-service.sh script

In the root directory of your project, create or update a `run-service.sh` script that allows you to easily start the service using docker compose.

## Run the service for testing

Navigate to the root directory of your project and run by the script to start the service

```bash
./run-service.sh <service-name> up
```

To stop the service, run:

```bash
./run-service.sh <service-name> down
```

Guarantee the service is running correctly by checking the logs or accessing the service through the exposed ports.

## Create a README.md file

In the service directory, create a `README.md` file that provides documentation for the service.

- Include a brief description of the service and its purpose.
- Include instructions on how to start, stop, and manage the service using docker compose commands.
- Provide any necessary configuration details or environment variable explanations.

## Update CLAUDE.md file

In the root directory of your project, create or update a `CLAUDE.md` file that provides an overview of the available services and instructions on how to use the `run-service.sh` script to manage the services.

## Update README.md file

In the root directory of your project, create or update a `README.md` file that provides an overview of the project and instructions on how to set up and manage the services using docker compose.
