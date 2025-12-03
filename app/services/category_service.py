from app.repositories.category_repo import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def get_categories(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_category(self, id: int):
        return self.repo.get_by_id(id)

    def create_category(self, data: CategoryCreate):
        return self.repo.create(data)

    def update_category(self, id: int, data: CategoryUpdate):
        return self.repo.update(id, data)

    def delete_category(self, id: int):
        return self.repo.delete(id)