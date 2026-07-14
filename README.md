# ⚡ Boilerplate FastAPI

Punto de partida para APIs REST con **FastAPI**, **PostgreSQL** y **SQLAlchemy 2.0**.  
Incluye DevContainers, validación con Pydantic, hashing con bcrypt y documentación Swagger automática.

---

## Stack

| Capa | Tecnología |
|------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 (mapped_column) |
| Validación | Pydantic v2 |
| Base de datos | PostgreSQL 17 |
| Hashing | bcrypt |
| Servidor | uvicorn |
| Entorno | Pipenv + DevContainers |
| Contenedores | Docker Compose |

---

## Estructura del proyecto

```
Boilerplate-FastAPI/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── dockerfile
│   └── docker-compose.yml
├── src/
│   ├── app.py                  # Punto de entrada FastAPI
│   ├── database.py             # Engine, SessionLocal, Base, get_db
│   └── api/
│       ├── __init__.py          # Registro de modelos
│       ├── router_global.py     # Router principal
│       └── users/
│           ├── __init__.py
│           ├── models.py        # Modelo SQLAlchemy
│           ├── schemas.py       # Schemas Pydantic
│           └── routes.py        # Endpoints CRUD
├── .env
├── .env.example
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Inicio rápido

### 1. Con DevContainers (recomendado)

1. Copia el archivo de entorno:
   ```bash
   cp .env.example .env
   ```

2. Abre el proyecto en VS Code y selecciona **"Reopen in Container"**.

3. Dentro del contenedor:
   ```bash
   pipenv install
   pipenv run start
   ```

4. Abre `http://localhost:3001/docs` para ver Swagger.

### 2. Sin DevContainers

1. Copia el archivo de entorno:
   ```bash
   cp .env.example .env
   ```

2. Instala dependencias:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. Levanta PostgreSQL (con Docker o local) y configura la `DATABASE_URL` en `.env`.

4. Arranca:
   ```bash
   pipenv run start
   ```

---

## Variables de entorno

```env
POSTGRES_USER=MGB
POSTGRES_DB=FastAPI
POSTGRES_PASSWORD=tu_password_seguro
DATABASE_URL=postgresql://MGB:tu_password_seguro@localhost:5432/FastAPI
```

---

## Endpoints incluidos

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/api/v1/users/` | Crear usuario |
| `GET` | `/api/v1/users/` | Listar usuarios |
| `GET` | `/api/v1/users/{id}` | Obtener usuario por ID |

Documentación interactiva disponible en:
- **Swagger UI** → `http://localhost:3001/docs`
- **ReDoc** → `http://localhost:3001/redoc`

---

## Cómo añadir un nuevo módulo

1. Crea la carpeta `src/api/tu_modulo/` con:
   - `__init__.py`
   - `models.py` — Modelo SQLAlchemy
   - `schemas.py` — Schemas Pydantic (Create, Response, Update)
   - `routes.py` — Endpoints con APIRouter

2. Registra el modelo en `src/api/__init__.py`:
   ```python
   from src.api.tu_modulo.models import TuModelo
   ```

3. Añade el router en `src/api/router_global.py`:
   ```python
   from src.api.tu_modulo.routes import router as tu_modulo_router
   api_router.include_router(tu_modulo_router, prefix="/tu_modulo", tags=["TuModulo"])
   ```

4. Reinicia uvicorn y el nuevo módulo aparece en `/docs`.

---

## Scripts disponibles

```toml
# Pipfile
[scripts]
start = "uvicorn src.app:app --reload --host 0.0.0.0 --port 3001"
```

```bash
pipenv run start    # Arranca el servidor en modo desarrollo
```

---

## Próximos pasos

- [ ] Configurar Alembic para migraciones
- [ ] Añadir autenticación JWT con `python-jose`
- [ ] Implementar endpoint de login
- [ ] Proteger rutas con `Depends(get_current_user)`
- [ ] Dockerizar para producción

---

## Autor

**Miguel Ángel García Bello**  
COEX CA-03 · Demarcación de Carreteras del Estado en Cádiz
