from fastapi import APIRouter, Depends
from .schemas import CategoryCreate, CategoryUpdate, CategoryOut
from .service import create_category, list_categories, get_category, update_category
from app.modules.auth.dependencies import ability_required

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", dependencies=[Depends(ability_required("categories:create"))])
async def create(data: CategoryCreate):
    return await create_category(data)

@router.get("/", response_model=list[CategoryOut], dependencies=[Depends(ability_required("categories:read"))])
async def get_all():
    return await list_categories()

@router.get("/{id}", response_model=CategoryOut, dependencies=[Depends(ability_required("categories:read"))])
async def view(id: int):
    return await get_category(id)

@router.put("/{id}", dependencies=[Depends(ability_required("categories:update"))])
async def update(id: int, data: CategoryUpdate):
    return await update_category(id, data)