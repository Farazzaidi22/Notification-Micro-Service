# app/db/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_PORT = os.getenv("DB_PORT", "5432")  # Update the port to 5432
DB_NAME = os.getenv("DB_NAME", "root")

# Use 'db' as the hostname to refer to the database service in Docker Compose
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@db:{DB_PORT}/{DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

# Define get_db here to avoid circular import issues
def get_db() -> Session:
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
