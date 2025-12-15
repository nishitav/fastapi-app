from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    is_active: bool = True

class CategoryUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

class CategoryOut(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True