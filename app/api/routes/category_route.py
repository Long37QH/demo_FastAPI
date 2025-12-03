from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.services.category_service import CategoryService
from app.api.dependencies import get_category_service

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[CategoryResponse])
def get_all(skip: int = 0, limit: int = 100, service: CategoryService = Depends(get_category_service)):
    return service.get_categories(skip, limit)

@router.get("/{id}", response_model=CategoryResponse)
def get_one(id: int, service: CategoryService = Depends(get_category_service)):
    category = service.get_category(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create(category: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return service.create_category(category)

@router.put("/{id}", response_model=CategoryResponse)
def update(id: int, category: CategoryUpdate, service: CategoryService = Depends(get_category_service)):
    updated_category = service.update_category(id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@router.delete("/{id}")
def delete(id: int, service: CategoryService = Depends(get_category_service)):
    success = service.delete_category(id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}