from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://expense-tracker-with-docker-1.onrender.com",
        "https://expense-tracker-lwms.onrender.com",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
    
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    if expense.idempotency_key:
        existing = db.query(models.Expense).filter(
            models.Expense.idempotency_key == expense.idempotency_key
        ).first()
        if existing:
            return existing

    obj = models.Expense(**expense.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@app.get("/expenses")
def get_expenses(category: str = None, sort: str = None, db: Session = Depends(get_db)):
    q = db.query(models.Expense)
    if category:
        q = q.filter(models.Expense.category == category)
    if sort == "date_desc":
        q = q.order_by(models.Expense.date.desc())

    data = q.all()
    total = sum(float(e.amount) for e in data)

    return {"data": data, "total": total}

@app.delete("/expenses/{id}")
def delete_expense(id: int, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == id).first()

    if not exp:
        return {"error": "Expense not found"}

    db.delete(exp)
    db.commit()
    return {"message": "Deleted successfully"}

@app.put("/expenses/{id}")
def update_expense(id: int, data: schemas.ExpenseUpdate, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == id).first()

    if not exp:
        return {"error": "Expense not found"}

    exp.amount = data.amount
    exp.category = data.category
    exp.description = data.description

    db.commit()
    db.refresh(exp)

    return {"message": "Updated successfully"}