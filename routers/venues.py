from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from models import Concerts

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()