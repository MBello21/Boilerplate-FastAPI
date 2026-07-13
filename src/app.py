import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router_global import api_router

app = FastAPI(
    title='Api modular FastAPI',
    description='Backend escalable',
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api/v1")


db_url = os.getenv("DATABASE_URL", "sqlite:////./test.db")
db_url = db_url.replace("postgres://", "postgresql://")
