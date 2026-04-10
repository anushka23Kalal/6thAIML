from pydantic import BaseModel
from fastapi import FastAPI  
app= FastAPI()
class Student(BaseModel):
  name:str
  age:int

Students=[]

@app.get("/student")
def get_student():
   return Students

@app.post("/student")
def create_student(student:Student):
   Students.append(student)
   return{"message":"Student created successfully"}
