from pydantic import BaseModel


class SYesId(BaseModel):
    id: int
    ok: bool = True


class SNoId(BaseModel):
    id: int
    ok: bool = False
