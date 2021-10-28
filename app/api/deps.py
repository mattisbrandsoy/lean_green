from typing import Generator
from app.db.session import SessionLocal


def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
