from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService
from app.api.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def get_all(skip: int = 0, limit: int = 100, service: ProductService = Depends(get_product_service)):
    return service.get_products(skip, limit)

@router.get("/{id}", response_model=ProductResponse)
def get_one(id: int, service: ProductService = Depends(get_product_service)):
    product = service.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    # Có thể thêm try/except IntegrityError nếu category_id không tồn tại
    return service.create_product(product)

@router.put("/{id}", response_model=ProductResponse)
def update(id: int, product: ProductUpdate, service: ProductService = Depends(get_product_service)):
    updated_product = service.update_product(id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{id}")
def delete(id: int, service: ProductService = Depends(get_product_service)):
    success = service.delete_product(id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}