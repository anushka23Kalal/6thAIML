from fastapi import FastAPI

app= FastAPI()
students=["Anushka","Divya","Shreya","Riya"]

@app.get("/student")
def get_student():
    return students

#Path parameter``
@app.get("/students/{id}")
def get_student_by_id(id:int):
    return {"student_name":students[id]}

#Post method
@app.post("/students")
def add_student(student:dict):
    students.append(student["name"])
    return{"message":"Success"}

#Query parameter
@app.get("/search/name")
def search_student(name:str):
    for student in students:
        if student==name:
            return{"message":"Student is found"}
    return{"message":"Student is not found"}
