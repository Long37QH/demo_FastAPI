from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def get_by_id(self, id: int):
        return self.db.query(Product).filter(Product.id == id).first()

    def create(self, product: ProductCreate):
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update(self, id: int, product_update: ProductUpdate):
        db_product = self.get_by_id(id)
        if not db_product:
            return None
        
        update_data = product_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
            
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete(self, id: int):
        db_product = self.get_by_id(id)
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True
        return False