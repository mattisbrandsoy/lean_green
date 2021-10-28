from typing import Any

from sqlalchemy.orm import declarative_base, declared_attr

@declarative_base
class Base:
    id: Any
    __name__: str

    # Autogen tablename
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
