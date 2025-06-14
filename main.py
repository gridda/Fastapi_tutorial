from fastapi import FastAPI
from pydantic import BaseModel
# Créer une application FastAPI
# إنشاء تطبيق FastAPI
app = FastAPI()
# Définir un modèle de données en utilisant Pydantic
# تعريف نمودج البيانات باستخدام Pydantic
class Student(BaseModel):
    id: int
    name: str
    grade: int
# Une liste pour stocker les données en mémoire
# قائمة لتخزين البيانات في الداكرة
students = [
    Student(id=1,name="Karim Ali",grade=5),
    Student(id=2,name="Khadija Ahmed",grade=3),
]
# Lecture de tous les articles
# قراءة جميع العناصر
@app.get("/students/")
def read_students():
    return students

# Créer un nouvel article
# انشاء عنصر جديد
@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

# Vous défiez un élément spécifique en fonction de son (ID) à l’aide de la méthode PUT
# تحديت عنصر معين بناء على معرفه (ID) باستخدام  Put method
@app.put("/student/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error": "Student not found"}

# Définir un élément spécifique en fonction de son (ID) à l’aide de la méthode DELETE
# حدف عنصر معين بناء على معرفه   (ID) باستخدام  DELETE method
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
            if student.id == student_id:
                del students[index]
                return {"message": "Student deleted"}   
    return {"error": "Student not found"} 