from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    # ✅ safer than Numeric in Render PostgreSQL
    amount = Column(Float, nullable=False)

    category = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    # ✅ keep as String (frontend sends YYYY-MM-DD)
    date = Column(String(20), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    