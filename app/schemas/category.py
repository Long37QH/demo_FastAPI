from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None  # Cho phép cập nhật từng phần

class CategoryResponse(CategoryBase):
    id: int
    class Config:
        orm_mode = True # Quan trọng để Pydantic đọc data từ SQLAlchemy model