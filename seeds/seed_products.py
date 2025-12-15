import os, sys
sys.path.insert(0, "/var/www/html/fastapi-app")

import asyncio
from app.core.database import SessionLocal
from app.modules.product.models import Product, product_category

products_to_insert = [
    {
        "name": "iPhone 15",
        "sku": "IP15",
        "price": 999.99,
        "description": "Latest Apple iPhone",
        "categories": [1, 2]
    },
    {
        "name": "Samsung Galaxy S24",
        "sku": "SGS24",
        "price": 899.99,
        "description": "Flagship Samsung phone",
        "categories": [1, 2]
    },
    {
        "name": "Dell XPS 13",
        "sku": "DX13",
        "price": 1299.99,
        "description": "High-end ultrabook",
        "categories": [1, 3]
    },
    {
        "name": "HP Pavilion 15",
        "sku": "HPP15",
        "price": 799.99,
        "description": "Mid-range laptop",
        "categories": [3]
    },
    {
        "name": "Sony WH-1000XM5",
        "sku": "SONXM5",
        "price": 349.99,
        "description": "Premium noise-cancelling headphones",
        "categories": [1, 5]
    },
    {
        "name": "AirPods Pro 2",
        "sku": "APP2",
        "price": 249.99,
        "description": "Apple wireless earbuds",
        "categories": [1, 5]
    },
    {
        "name": "LG OLED 55 TV",
        "sku": "LGOLED55",
        "price": 1499.99,
        "description": "OLED Smart TV",
        "categories": [4]
    },
    {
        "name": "Nikon D5600",
        "sku": "NIKD5600",
        "price": 699.99,
        "description": "DSLR Camera",
        "categories": [1]
    },
    {
        "name": "KitchenAid Mixer",
        "sku": "KAMIX",
        "price": 299.99,
        "description": "Home kitchen mixer",
        "categories": [4]
    },
    {
        "name": "Logitech MX Master 3",
        "sku": "MXM3",
        "price": 119.99,
        "description": "Wireless ergonomic mouse",
        "categories": [1, 5]
    },
]

async def seed_products():
    async with SessionLocal() as db:
        for item in products_to_insert:
            p = Product(
                name=item["name"],
                sku=item["sku"],
                price=item["price"],
                description=item["description"],
                is_active=True
            )
            db.add(p)
            await db.flush()

            # Insert pivot table records
            for cid in item["categories"]:
                await db.execute(
                    product_category.insert().values(product_id=p.id, category_id=cid)
                )

        await db.commit()
        print("10 products inserted successfully!")

if __name__ == "__main__":
    asyncio.run(seed_products())
