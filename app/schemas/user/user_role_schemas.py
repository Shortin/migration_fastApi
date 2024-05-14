from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SUserRoleAdd(BaseModel):
    name: str = Field(max_length=50)


class SUserRoleUpdate(BaseModel):
    name: Optional[str] = Field(max_length=50)


class SUserRole(SUserRoleAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

