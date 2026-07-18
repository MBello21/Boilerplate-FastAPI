# FastAPI Boilerplate

Plantilla base para proyectos con FastAPI, SQLAlchemy 2.0 y PostgreSQL.

## Stack

- FastAPI
- SQLAlchemy 2.0 (Mapped)
- Pydantic v2
- PostgreSQL
- Passlib (bcrypt)

## Estructura
src/
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── app.py
│   ├── database.py
│   └── router_global.py
├── .env.example
└── Pipfile
## Setup

```bash
pipenv install
cp .env.example .env
pipenv run uvicorn src.app.app:app --reload
```
