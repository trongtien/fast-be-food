from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class LoginRequest(BaseModel):
    username: str
    password: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"}


@app.post("/login", tags=["login"])
async def login( login_request: LoginRequest):
    return {
        "id": 1,
        "name": "admin",
        "avartar": "https://gravatar.com/avatar/bfc048fe6df7d1b3ab23762ff20e11eb?s=400&d=retro&r=x",
        "role": "owner",
        "token": "jhmgIDvk4kyj62iGgmYYnQ==",
        "menu": [
            { "id": "1", "name": 'Dashboard', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "2", "name": 'products', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [
                    { "id": "2.1", "name": 'Products=Analytics', "icon": "UserOutlined", "path": "/products-analytics", "code": "products-analytics", "subMenu": [] },
                    { "id": "2.2", "name": 'Products=Schedule', "icon": "AppstoreOutlined", "path": "/products-schedule", "code": "products-schedule", "subMenu": [] }
                ] 
            },
            { "id": "3", "name": 'analytics', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "4", "name": 'schedule', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] }
        ]
    }


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": " Student deleted successfully"}
