import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://expense_db_aovt_user:WchyxnySanXwgStsGmDvI8TG6l0l4eC3@dpg-d7so2ihkh4rs73980ha0-a.singapore-postgres.render.com/expense_db_aovt"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()