from fastapi import FastAPI
from schemas import CourseCreate

app = FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.get("/")
async def root():
    return {
        "message": "API running"
    }


@app.post("/api/courses/")
async def create_course(course: CourseCreate):
    return {
        "message": "Course created",
        "course": course
    }

from typing import Optional

from pydantic import BaseModel


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True

