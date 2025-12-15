from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.models_base import Base
from app.modules.category.models import Category

product_category = Table(
    "product_category",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    sku = Column(String(255))
    price = Column(Float)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)

    categories = relationship("Category", secondary=product_category)
