import os, sys
sys.path.insert(0, "/var/www/html/fastapi-app")

import asyncio
from app.core.database import SessionLocal
from app.modules.category.models import Category

async def seed_categories():
    async with SessionLocal() as db:
        categories = [
            Category(name="Electronics", is_active=True),
            Category(name="Mobiles", is_active=True),
            Category(name="Laptops", is_active=True),
            Category(name="Home Appliances", is_active=True),
            Category(name="Accessories", is_active=True),
        ]

        db.add_all(categories)
        await db.commit()
        print("5 categories inserted successfully!")

if __name__ == "__main__":
    asyncio.run(seed_categories())
