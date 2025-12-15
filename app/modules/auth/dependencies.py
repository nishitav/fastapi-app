from fastapi import Header, HTTPException, Depends
from app.core.database import SessionLocal
from .models import Token, User

async def get_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing token")

    token_str = authorization.split(" ")[1]

    async with SessionLocal() as db:
        query = await db.execute(
            Token.__table__.select().where(Token.token == token_str)
        )
        token = query.fetchone()

        if not token:
            raise HTTPException(401, "Invalid token")

        return token._mapping

def ability_required(ability: str):
    async def checker(db_token = Depends(get_token)):
        abilities = db_token["abilities"].split(",")
        if ability not in abilities:
            raise HTTPException(403, "Missing ability")
        return True
    return checker
