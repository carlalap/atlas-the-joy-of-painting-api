"""Initiate Database for using in other models"""
from engine.db import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator


def get_database() -> Generator:
    """ Create and return database session and close properly when is done """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
