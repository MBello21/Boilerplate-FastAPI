# ConstruCloudAI API

Backend de ConstruCloudAI — plataforma de generación de presupuestos de construcción asistidos por IA.

## Stack

- **Runtime:** Python 3.12+
- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0 + Alembic (migraciones)
- **Base de datos:** PostgreSQL 16
- **Autenticación:** JWT (access + refresh tokens)
- **IA:** Integración con LLM para sugerencia de partidas y estimaciones
- **Storage:** MinIO (fase posterior al MVP)
- **Containerización:** Docker + Docker Compose

## Estructura del proyecto

```
construcloudai-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point FastAPI
│   ├── config.py               # Settings (Pydantic BaseSettings)
│   ├── database.py             # Engine, SessionLocal, Base
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── cliente.py
│   │   ├── presupuesto.py
│   │   ├── detalle.py
│   │   └── tarifa_base.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── cliente.py
│   │   ├── presupuesto.py
│   │   ├── detalle.py
│   │   └── tarifa_base.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── usuarios.py
│   │   ├── clientes.py
│   │   ├── presupuestos.py
│   │   ├── detalles.py
│   │   ├── tarifas.py
│   │   └── ia.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── presupuesto_service.py
│   │   ├── ia_service.py
│   │   └── pdf_service.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py         # JWT, hashing
│   │   └── dependencies.py     # get_db, get_current_user
│   └── utils/
│       ├── __init__.py
│       └── exceptions.py
├── alembic/
│   ├── env.py
│   └── versions/
├── tests/
│   └── __init__.py
├── alembic.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Setup local

```bash
# Clonar
git clone git@github.com:tu-usuario/construcloudai-api.git
cd construcloudai-api

# Entorno virtual
python -m venv venv
source venv/bin/activate

# Dependencias
pip install -r requirements.txt

# Variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Base de datos
docker compose up -d db
alembic upgrade head

# Servidor de desarrollo
uvicorn app.main:app --reload --port 8000
```

## Deploy

Desplegado en Proxmox (homelab) con Docker Compose.

## Licencia

Proyecto privado — Labs by 4Geeks Academy (Jul–Ago 2026).