from app.core.database import SessionLocal
from .models import Category
from fastapi import HTTPException
from sqlalchemy import select

async def create_category(data):
    async with SessionLocal() as db:
        c = Category(**data.dict())
        db.add(c)
        await db.commit()
        return c

async def list_categories():
    async with SessionLocal() as db:
        result = await db.execute(select(Category))
        return result.scalars().all()

async def get_category(id: int):
    async with SessionLocal() as db:
        result = await db.execute(
            select(Category).where(Category.id == id)
        )
        category = result.scalar_one_or_none()
        
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        return category

async def update_category(id: int, data):
    async with SessionLocal() as db:
        # get ORM model
        result = await db.execute(select(Category).where(Category.id == id))
        category = result.scalar_one_or_none()
        
        if not category:
            raise HTTPException(404, "Category not found")

        # update fields
        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(category, key, value)

        await db.commit()
        await db.refresh(category)
        return category
