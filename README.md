# Expense Tracker (Production Ready)

## Tech
- FastAPI
- PostgreSQL
- SQLAlchemy
- Vanilla JS frontend

## Setup

### 1. Create DB
CREATE DATABASE expenses;

### 2. Env
set DATABASE_URL=postgresql://postgres:password@localhost:5432/expenses

### 3. Run
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Open frontend/index.html

## Notes
- Uses DECIMAL for money (no float issues)
- Idempotency prevents duplicate requests
