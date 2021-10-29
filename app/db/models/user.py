from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, Field, EmailStr
from ..base_class import Base

# if TYPE_CHECKING:
#     from .team_model import Team

class User(Base):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key = True)
    email: EmailStr
    name: str
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False
