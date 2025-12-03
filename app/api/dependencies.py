from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.repositories.category_repo import CategoryRepository
from app.services.category_service import CategoryService
from app.repositories.product_repo import ProductRepository
from app.services.product_service import ProductService

# --- CATEGORY DI ---
def get_category_repo(db: Session = Depends(get_db)) -> CategoryRepository:
    return CategoryRepository(db)

def get_category_service(repo: CategoryRepository = Depends(get_category_repo)) -> CategoryService:
    return CategoryService(repo)

# --- PRODUCT DI ---
def get_product_repo(db: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db)

def get_product_service(repo: ProductRepository = Depends(get_product_repo)) -> ProductService:
    return ProductService(repo)