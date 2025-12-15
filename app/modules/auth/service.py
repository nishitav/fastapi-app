from uuid import uuid4
from fastapi import HTTPException
from app.core.database import SessionLocal
from app.core.security import hash_password, verify_password, create_token
from .models import User, Token

DEFAULT_ABILITIES = ["categories:read", "products:read"]

async def register_user(data):
    async with SessionLocal() as db:
        new_user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password),
        )
        db.add(new_user)
        await db.commit()
        return {"message": "User registered"}

async def login_user(data):
    async with SessionLocal() as db:
        query = await db.execute(User.__table__.select().where(User.email == data.email))
        user = query.fetchone()

        if not user:
            raise HTTPException(400, "Invalid email")

        user = user._mapping

        if not verify_password(data.password, user["password"]):
            raise HTTPException(400, "Invalid password")

        raw_token = str(uuid4())

        db_token = Token(
            user_id=user["id"],
            token=raw_token,
            abilities=",".join(DEFAULT_ABILITIES)
        )
        db.add(db_token)
        await db.commit()

        return {"token": raw_token, "abilities": DEFAULT_ABILITIES}

async def logout_current(token_id):
    async with SessionLocal() as db:
        await db.execute(Token.__table__.delete().where(Token.id == token_id))
        await db.commit()
        return {"message": "Logged out"}

async def logout_all(user_id):
    async with SessionLocal() as db:
        await db.execute(Token.__table__.delete().where(Token.user_id == user_id))
        await db.commit()
        return {"message": "Logged out from all devices"}
