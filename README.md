# 💪 WorkoutApp Backend (UPDATED DAILY)

A RESTful API backend for a workout tracking application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. Features JWT authentication, role-based access control, workout logging, and progress tracking.

# A frontend will be made soon using  React.js and other languages! 

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **FastAPI** | Web framework & API |
| **PostgreSQL** | Database |
| **SQLAlchemy** | ORM |
| **Alembic** | Database migrations |
| **Pydantic v2** | Data validation & schemas |
| **python-jose** | JWT token generation & verification |
| **passlib + bcrypt** | Password hashing |
| **uv** | Package management |
| **uvicorn** | ASGI server |

---

## 📁 Project Structure

```
WorkoutApp-Backend/
├── app/
│   ├── main.py               # App entry point, router registration
│   ├── core/
│   │   ├── config.py         # Environment variable settings
│   │   ├── oauth2.py         # JWT creation, verification, role guard
│   │   └── utils.py          # Password hashing helpers
│   ├── database/
│   │   └── database.py       # SQLAlchemy engine & session setup
│   ├── model/
│   │   └── model.py          # Database models (Users, Workout, Progress)
│   ├── routers/
│   │   ├── auth.py           # Login endpoint
│   │   ├── user_router.py    # User registration & workout retrieval
│   │   ├── workouts.py       # Workout CRUD
│   │   ├── progress.py       # Progress/goals tracking
│   │   └── admin.py          # Admin-only endpoints
│   └── schemas/
│       └── schemas.py        # Pydantic request/response models
├── Alembic/                  # Migration files
├── alembic.ini               # Alembic config
├── pyproject.toml
├── requirements.txt
└── .env                      # Environment variables (not committed)
```

---

## 🚀 Setup Guide

### Prerequisites

- Python 3.12+
- PostgreSQL running locally (or a hosted instance)
- `uv` installed — `pip install uv`

---

### 1. Clone the repository

```bash
git clone https://github.com/WafflesDevs/WorkoutApp-Backend.git
cd WorkoutApp-Backend
```

### 2. Install dependencies

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

Create a `.env` file in the root directory with the following:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=workoutapp
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=yourpassword

SECRET_KEY=your-secret-key-here
ALGO=HS256
TOKEN_EXPIRE=30
```

> **Tip:** Generate a strong secret key with `openssl rand -hex 32`

### 4. Set up the database

Make sure your PostgreSQL server is running and the database exists:

```sql
CREATE DATABASE workoutapp;
```

Then run Alembic migrations to create all tables:

```bash
alembic upgrade head
```

### 5. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be live at **`http://localhost:8000`**

Interactive docs available at **`http://localhost:8000/docs`**

---

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/login` | Login and receive a JWT token | ❌ |

**Login request body:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

**Response:**
```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

---

### 👤 Users

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/users/create_user` | Register a new user | ❌ |
| `GET` | `/users/user/workouts` | Get all workouts for the logged-in user | ✅ |

**Register request body:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword",
  "role": "User"
}
```

---

### 🏋️ Workouts

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/workout` | Log a new workout | ✅ |
| `PUT` | `/workout/{id}` | Update an existing workout | ✅ |
| `DELETE` | `/workout/{id}` | Delete a workout | ✅ |
| `GET` | `/workouts` | Provides a Preset List of Workouts | ❌ |

**Workout request body:**
```json
{
  "type": "Bench Press",
  "weight": 100,
  "reps": 8,
  "sets": 4
}
```

---

### 📈 Progress

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/createprogress` | Create a progress/goals entry | ✅ |
| `GET` | `/progress` | Get your current progress | ✅ |
| `PUT` | `/progress/{id}` | Update your progress entry | ✅ |

**Progress request body:**
```json
{
  "goal_workouts": 20,
  "biggest_weight": 120,
  "goal_weight": 150
}
```

---

### 🛡 Admin

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/allworkouts?userid_search={id}` | View all workouts for any user | ✅ Admin only |
| `GET` | `/allusers` | Get a list of all registered users | ✅ Admin only |
| `PUT` | `/roleupdate` | Update a user's role | ✅ Admin only |

**Get all users response:**
```json
[
  {
    "user_id": 1,
    "email": "user@example.com",
    "created_at": "2026-06-25T00:00:00",
    "role": "User"
  }
]
```

**Role update request body:**
```json
{
  "user_id": 2,
  "role": "Admin"
}
```

> **Note:** Admins cannot update their own role.

---

## 🔒 Authentication & Roles

All protected routes require a Bearer token in the `Authorization` header:

```
Authorization: Bearer <your_token>
```

The app supports two roles:

| Role | Access |
|------|--------|
| `User` | Can manage their own workouts and progress |
| `Admin` | Can view workouts for any user |

Role is set at registration and embedded in the JWT token.

---

## 🗄 Database Models

### Users
| Column | Type | Notes |
|--------|------|-------|
| `user_id` | Integer | Primary key |
| `email` | String | Unique |
| `password` | String | Bcrypt hashed |
| `role` | String | `"User"` or `"Admin"` |
| `created_at` | Timestamp | Auto-set |

### Workouts
| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer | Primary key |
| `owner_id` | Integer | FK → users.user_id |
| `type` | String | e.g. "Bench Press" |
| `weight` | Integer | In kg/lbs |
| `reps` | Integer | |
| `sets` | Integer | |
| `created_at` | Timestamp | Auto-set |

### Progress
| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer | Primary key |
| `owner_id` | Integer | FK → users.user_id |
| `goal_workouts` | Integer | Target workout count |
| `biggest_weight` | Integer | Current max weight lifted |
| `goal_weight` | Integer | Target weight |
| `created_at` | Timestamp | Auto-set |

---

## 🗃 Database Migrations (Alembic)

```bash
# Apply all migrations
alembic upgrade head

# Create a new migration after changing models
alembic revision --autogenerate -m "your description"

# Roll back one migration
alembic downgrade -1
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

MIT — free to use and modify.
