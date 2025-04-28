from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserLogin
from base import SessionLocal
from auth.auth import create_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login/", tags = ["Login"])
def user_login(user : UserLogin , db: Session = Depends(get_db)):
    user_new = db.query(User).filter(User.email == user.email).first()
    if not user_new or not user.password == user_new.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_token({
        "usermail": user.email,
        "role" : user_new.role,
        "id" : user_new.user_id
    })
    return {"access_token": access_token, "token_type": "bearer"}