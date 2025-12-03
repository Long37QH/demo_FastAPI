from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.routes import category_route, product_route # <--- Import thêm

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Layered Architecture Demo")

app.include_router(category_route.router)
app.include_router(product_route.router) # <--- Đăng ký thêm

@app.get("/")
def root():
    return {"message": "CRUD API with Layered Architecture"}