from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

expenses = []

@app.get("/")
def home():
    return {"message": "API running"}

# GET expenses
@app.get("/expenses")
def get_expenses():
    total = sum(float(e.get("amount", 0)) for e in expenses)
    return {
        "data": expenses,
        "total": total
    }

# POST add expense
@app.post("/expenses")
def add_expense(expense: dict):
    required_fields = ["amount", "category", "description", "date"]

    for field in required_fields:
        if field not in expense:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    expenses.append(expense)

    return {
        "message": "Expense added successfully",
        "data": expense
    }

# DELETE
@app.delete("/expenses/{index}")
def delete_expense(index: int):
    if index < 0 or index >= len(expenses):
        raise HTTPException(status_code=400, detail="Invalid index")

    deleted = expenses.pop(index)

    return {
        "message": "Deleted successfully",
        "data": deleted
    }

# UPDATE
@app.put("/expenses/{index}")
def update_expense(index: int, data: dict):
    if index < 0 or index >= len(expenses):
        raise HTTPException(status_code=400, detail="Invalid index")

    expenses[index] = data

    return {
        "message": "Updated successfully",
        "data": data
    }