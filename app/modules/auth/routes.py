from fastapi import APIRouter, Depends
from .schemas import UserCreate, UserLogin, TokenResponse
from .service import register_user, login_user, logout_current, logout_all
from .dependencies import get_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(data: UserCreate):
    return await register_user(data)

@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    return await login_user(data)

@router.post("/logout")
async def logout(token = Depends(get_token)):
    return await logout_current(token["id"])

@router.post("/logout-all")
async def logout_all_devices(token = Depends(get_token)):
    return await logout_all(token["user_id"])
