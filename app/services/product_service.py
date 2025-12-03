from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_products(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_product(self, id: int):
        return self.repo.get_by_id(id)

    def create_product(self, data: ProductCreate):
        # Có thể check category_id tồn tại ở đây nếu cần logic phức tạp
        return self.repo.create(data)

    def update_product(self, id: int, data: ProductUpdate):
        return self.repo.update(id, data)

    def delete_product(self, id: int):
        return self.repo.delete(id)