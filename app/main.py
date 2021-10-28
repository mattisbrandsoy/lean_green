import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.db.session import engine
from app.db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url="/openapi.json",
    )
    app.include_router(api_router)
    create_tables()
    return app


app = start_application()