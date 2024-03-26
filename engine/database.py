"""Sets up the database connection using SQLite"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database URL for SQLite (file-based database)
SQLALCHEMY_DATABASE_URL = "sqlite:///jop_database.db"
# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})
# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a Base class for defining database models
Base = declarative_base()
