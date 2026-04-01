# llm-poc

Small Python project that must be run with Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Run the application

Build and start the app (auto-reloads on Python file changes via `watchfiles`):

```bash
docker compose up --build
```

## Run tests

Run tests inside the app container:

```bash
docker compose run --rm app python3 -m pytest -q
```
