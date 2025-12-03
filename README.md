# FastAPI Layered Architecture Demo

Dự án mẫu xây dựng RESTful API với **FastAPI** sử dụng kiến trúc phân lớp (**Layered Architecture**) và **Dependency Injection (DI)**. Dự án bao gồm các chức năng CRUD cơ bản cho `Category` và `Product`.

## 🚀 Tính năng

* **Kiến trúc phân lớp:** Routes -> Service -> Repository -> Database.
* **Dependency Injection:** Quản lý phụ thuộc lỏng lẻo (loose coupling), dễ dàng mở rộng và test.
* **Database:** Sử dụng SQLite (mặc định) với SQLAlchemy ORM.
* **Validation:** Sử dụng Pydantic Schemas.
* **Tài liệu API:** Tự động tích hợp Swagger UI và ReDoc.

## 🛠 Cấu trúc dự án

```text
fastapi_layered_demo/
├── app/
│   ├── api/                 # Routes & Dependencies (Controller Layer)
│   ├── core/                # Database config & settings
│   ├── models/              # SQLAlchemy Models (Database Entities)
│   ├── repositories/        # Database Access Layer (CRUD queries)
│   ├── schemas/             # Pydantic Models (Data Transfer Objects)
│   ├── services/            # Business Logic Layer
│   └── main.py              # App entry point
├── requirements.txt         # Danh sách thư viện
└── README.md                # Tài liệu hướng dẫn
