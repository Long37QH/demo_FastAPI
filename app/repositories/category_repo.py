from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Category).offset(skip).limit(limit).all()

    def get_by_id(self, id: int):
        return self.db.query(Category).filter(Category.id == id).first()

    def create(self, category: CategoryCreate):
        db_category = Category(name=category.name)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def update(self, id: int, category_update: CategoryUpdate):
        db_category = self.get_by_id(id)
        if not db_category:
            return None
        
        # Chỉ cập nhật các trường được gửi lên
        update_data = category_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)
            
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def delete(self, id: int):
        db_category = self.get_by_id(id)
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        return False