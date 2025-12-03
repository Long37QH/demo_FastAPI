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

⚙️ Yêu cầu hệ thống
Python 3.8 trở lên

Git

📦 Hướng dẫn cài đặt
Làm theo các bước sau để cài đặt dự án trên máy mới:

1. Clone dự án
Bash

git clone <đường-link-git-của-bạn>
cd fastapi_layered_demo
2. Tạo môi trường ảo (Virtual Environment)
Khuyến khích sử dụng môi trường ảo để tránh xung đột thư viện.

Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate
3. Cài đặt thư viện
Bash

pip install -r requirements.txt
▶️ Hướng dẫn chạy dự án
Khởi chạy server development:

Bash

uvicorn app.main:app --reload
Server sẽ chạy tại địa chỉ: http://127.0.0.1:8000

Lưu ý: File database test.db sẽ tự động được tạo khi chạy lần đầu tiên.

📚 Tài liệu API (Documentation)
Sau khi chạy server, bạn có thể truy cập tài liệu API tự động tại:

Swagger UI (Test trực tiếp): http://127.0.0.1:8000/docs

ReDoc (Xem chi tiết): http://127.0.0.1:8000/redoc

🧪 Ví dụ Test API (JSON Body)
1. Tạo Category mới (POST /categories/)

JSON

{
  "name": "Laptop"
}
2. Tạo Product mới (POST /products/) Lưu ý: category_id phải tồn tại trước đó.

JSON

{
  "name": "MacBook Pro M1",
  "price": 30000000,
  "category_id": 1
}
🤝 Đóng góp
Nếu bạn muốn đóng góp, vui lòng tạo Pull Request hoặc mở Issue.


---

### Mẹo hiển thị trên Github/Gitlab
File `README.md` này sử dụng cú pháp **Markdown**. Khi bạn đẩy lên Github, Gitlab ho
