from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SUserAdd(BaseModel):
    email: str = Field(max_length=50)
    username: str = Field(max_length=100)
    password: str = Field(max_length=25)
    user_role_id: int


class UserUpdate(BaseModel):
    email: Optional[str] = Field(max_length=50)
    username: Optional[str] = Field(max_length=100)
    password: Optional[str] = Field(max_length=25)
    user_role_id: Optional[int]


class SUser(SUserAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

