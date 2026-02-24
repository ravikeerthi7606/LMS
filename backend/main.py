from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from auth import router as auth_router
from lecturer import router as lecturer_router
from student import router as student_router


app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

app.mount("/videos", StaticFiles(directory="uploads"), name="videos")


app.include_router(auth_router)
app.include_router(lecturer_router)
app.include_router(student_router)

