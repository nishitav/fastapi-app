from fastapi import APIRouter, Depends
from .schemas import ProductCreate, ProductUpdate
from .service import create_product, list_products
from app.modules.auth.dependencies import ability_required

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", dependencies=[Depends(ability_required("products:create"))])
async def create(data: ProductCreate):
    return await create_product(data)

@router.get("/", dependencies=[Depends(ability_required("products:read"))])
async def get_all():
    return await list_products()

@router.get("/{id}", dependencies=[Depends(ability_required("products:read"))])
async def view(id: int):
    return await get_product(id)

@router.put("/{id}", dependencies=[Depends(ability_required("products:update"))])
async def update(id: int, data: ProductUpdate):
    return await update_product(id, data)