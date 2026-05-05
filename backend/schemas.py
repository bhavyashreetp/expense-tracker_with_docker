from pydantic import BaseModel, Field
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    category: str
    description: Optional[str] = ""
    date: str
    idempotency_key: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str
    date: str

    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    amount: float
    category: str
    description: str
