from fastapi import APIRouter, UploadFile, File, Form
import shutil
from database import courses_collection

router = APIRouter()

@router.post("/upload-course")
def upload_course(
    title: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    video: UploadFile = File(...)
):
    file_path = f"uploads/{video.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    course = {
        "title": title,
        "description": description,
        "price": price,
        "video_url": file_path,
        "students_enrolled": 0,
        "rating": 0
    }

    courses_collection.insert_one(course)

    return {"message": "Course uploaded"}