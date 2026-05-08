import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

# 🚨 FAIL FAST (IMPORTANT FOR DEBUGGING)
if not DATABASE_URL:
    raise Exception("DATABASE_URL not set in environment variables")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args={"sslmode": "require"}  # ✅ REQUIRED for Render PostgreSQL
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()