from fastapi import APIRouter
from database import courses_collection, purchases_collection

router = APIRouter()

@router.get("/courses")
def get_courses():
    courses = list(courses_collection.find({}, {"_id": 0}))
    return courses

@router.post("/purchase")
def purchase(data: dict):
    purchases_collection.insert_one(data)
    return {"message": "Course purchased"}