from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.webstats import WebStats
from schemas.webstats import WebStatsResponse
from base import SessionLocal
from auth.auth import decode_token


router = APIRouter()

roles = ['Admin', 'admin']

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get_stats/", response_model=list[WebStatsResponse])
def get_website_URLs(db: Session = Depends(get_db), cred = Depends(decode_token)):
    return db.query(WebStats).all()
