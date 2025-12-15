# FastAPI + MySQL + SQLAlchemy + Alembic + Token Auth (Laravel Sanctum Style)

A production-ready backend boilerplate built with FastAPI, featuring MySQL integration via SQLAlchemy, database migrations with Alembic, and token-based authentication inspired by Laravel Sanctum.

A clean, modular FastAPI backend following a Laravel-like structure with:

- Token-based authentication  
- Role → Ability permission system  
- Category CRUD  
- Product CRUD (with multiple categories)  
- SQLAlchemy ORM  
- Alembic migrations  
- Seeders (users, categories, products)  
- Modular folder architecture  

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend Framework | FastAPI |
| Language | Python 3.12 |
| Database | MySQL |
| ORM | SQLAlchemy (async) |
| Migrations | Alembic |
| Auth | Token-based (custom Sanctum-like) |

---

## 📥 Installation

### 1. Clone repo

```bash
git clone https://github.com/your-name/your-repo.git
cd fastapi-app
```

### 2. Configure MySQL Database
```bash
CREATE DATABASE fastapi_db CHARACTER SET utf8mb4;
```

### 3. Run Migrations
```bash
alembic revision --autogenerate -m "initial tables"
alembic upgrade head
```

### 3. Run Seeders
```bash
python3 seeds/seed_users.py
python3 seeds/seed_categories.py
python3 seeds/seed_products.py
```

## ▶️ Start FastAPI Server

```bash
uvicorn app.main:app --reload
```
http://127.0.0.1:8000

http://127.0.0.1:8000/docs  (Swagger API)


## 🔐 Authentication

Login endpoint:
```bash
POST /auth/login
```

Payload:
```bash
{
  "email": "admin@example.com",
  "password": "password123"
}
```

Response:
```bash
{
  "token": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "abilities": ["categories:read", "products:read", ...]
}
```


Use this token in Postman:
```bash
Authorization: Bearer <token>
```