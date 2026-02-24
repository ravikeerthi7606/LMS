from fastapi import APIRouter, HTTPException
from database import users_collection
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "secret"

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=2)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

@router.post("/signup")
def signup(user: dict):
    user["password"] = hash_password(user["password"])
    users_collection.insert_one(user)
    return {"message": "User created"}

@router.post("/login")
def login(user: dict):
    db_user = users_collection.find_one({"email": user["email"]})
    
    if not db_user or not verify_password(user["password"], db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({
        "email": db_user["email"],
        "role": db_user["role"]
    })

    return {"token": token, "role": db_user["role"]}