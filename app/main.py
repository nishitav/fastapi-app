from fastapi import FastAPI
from app.core.database import init_db
from app.modules.auth.routes import router as AuthRouter
from app.modules.category.routes import router as CategoryRouter
from app.modules.product.routes import router as ProductRouter

app = FastAPI(title="FastAPI Sanctum Style Auth")

app.include_router(AuthRouter)
app.include_router(CategoryRouter)
app.include_router(ProductRouter)

@app.on_event("startup")
async def startup():
    await init_db()
