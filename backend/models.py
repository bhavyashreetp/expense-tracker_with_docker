from sqlalchemy import Column, Integer, String, DateTime, Numeric
from datetime import datetime
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10,2), nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    date = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    idempotency_key = Column(String, unique=True)
