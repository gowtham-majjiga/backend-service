# Backend Service

Production-style REST API demonstrating clean backend architecture, validation, persistence, structured errors, testing, and Dockerized development.

## Architecture

```text
Client → Router → Validation → Service → Repository → Database
```

## Features

- RESTful CRUD API
- Request/response validation with Pydantic
- SQLAlchemy persistence layer
- Service/repository separation
- Pagination and filtering
- Consistent error responses
- Authentication-ready dependency boundary
- Unit and API tests
- Docker support
- OpenAPI/Swagger documentation

## Stack

Python · FastAPI · SQLAlchemy · SQLite/PostgreSQL · Pydantic · pytest · Docker

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs` for the interactive API documentation.

## Endpoints

```text
GET    /health
GET    /api/v1/items
POST   /api/v1/items
GET    /api/v1/items/{id}
PATCH  /api/v1/items/{id}
DELETE /api/v1/items/{id}
```

## Engineering decisions

HTTP concerns are kept in routers, business rules in services, and persistence behind repositories. This makes the application easier to test and extend without coupling API handlers to the database.

## Security notes

Secrets belong in environment variables. Authentication is isolated behind a dependency boundary so JWT/OAuth can be introduced without rewriting business logic.
