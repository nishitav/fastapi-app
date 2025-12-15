import os
import sys

# Add project root to PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

import asyncio
from app.core.database import SessionLocal
from app.core.security import hash_password
from app.modules.auth.models import User

async def seed_users():
    async with SessionLocal() as db:
        user = User(
            name="Admin User",
            email="admin@example.com",
            password=hash_password("password123")
        )
        db.add(user)
        await db.commit()
        print("User seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_users())
