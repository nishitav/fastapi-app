from app.core.database import SessionLocal
from .models import Product, product_category
from fastapi import HTTPException

async def create_product(data):
    async with SessionLocal() as db:
        p = Product(
            name=data.name,
            sku=data.sku,
            price=data.price,
            description=data.description,
            is_active=data.is_active,
        )
        db.add(p)
        await db.flush()

        for cid in data.category_ids:
            await db.execute(
                product_category.insert().values(product_id=p.id, category_id=cid)
            )

        await db.commit()
        return p

async def list_products():
    async with SessionLocal() as db:
        result = await db.execute(Product.__table__.select())
        return result.fetchall()

async def get_product(id: int):
    async with SessionLocal() as db:
        result = await db.execute(
            Product.__table__.select().where(Product.id == id)
        )
        p = result.fetchone()
        if not p:
            raise HTTPException(404, "Product not found")
        return p._mapping

async def update_product(id: int, data):
    async with SessionLocal() as db:
        result = await db.execute(
            Product.__table__.select().where(Product.id == id)
        )
        p = result.fetchone()
        if not p:
            raise HTTPException(404, "Product not found")

        update_data = data.dict(exclude_unset=True)

        # update basic fields
        basic_fields = {k: v for k, v in update_data.items() if k != "category_ids"}

        if basic_fields:
            await db.execute(
                Product.__table__.update()
                .where(Product.id == id)
                .values(**basic_fields)
            )

        # update categories if provided
        if "category_ids" in update_data:
            # delete old category relations
            await db.execute(
                product_category.delete().where(product_category.c.product_id == id)
            )

            # insert new category relations
            for cid in update_data["category_ids"]:
                await db.execute(
                    product_category.insert().values(product_id=id, category_id=cid)
                )

        await db.commit()

        # return updated
        updated = await db.execute(
            Product.__table__.select().where(Product.id == id)
        )
        return updated.fetchone()._mapping
