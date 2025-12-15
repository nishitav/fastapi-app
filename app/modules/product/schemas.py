from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    description: str
    category_ids: List[int]
    is_active: bool = True

class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    price: float | None = None
    description: str | None = None
    category_ids: List[int] | None = None
    is_active: bool | None = None