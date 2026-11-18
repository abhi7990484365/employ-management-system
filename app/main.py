import sqlite3
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, Field
from app.database import connect, initialize

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize()
    yield

app = FastAPI(title="Employee Management API", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class Employee(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)

@app.get("/", include_in_schema=False)
def home():
    return FileResponse("app/static/index.html")

@app.get("/api/employees")
def list_employees(search: str | None = Query(default=None)):
    with connect() as db:
        if search:
            rows = db.execute("SELECT * FROM employees WHERE name LIKE ? ORDER BY id DESC", (f"%{search}%",)).fetchall()
        else:
            rows = db.execute("SELECT * FROM employees ORDER BY id DESC").fetchall()
    return [dict(row) for row in rows]

@app.post("/api/employees", status_code=201)
def create_employee(employee: Employee):
    try:
        with connect() as db:
            cur = db.execute("INSERT INTO employees(name,email,department) VALUES(?,?,?)",
                             (employee.name.strip(), str(employee.email).lower(), employee.department.strip()))
            row = db.execute("SELECT * FROM employees WHERE id=?", (cur.lastrowid,)).fetchone()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="An employee with this email already exists")

@app.put("/api/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    try:
        with connect() as db:
            cur = db.execute("UPDATE employees SET name=?,email=?,department=? WHERE id=?",
                             (employee.name.strip(), str(employee.email).lower(), employee.department.strip(), employee_id))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Employee not found")
            row = db.execute("SELECT * FROM employees WHERE id=?", (employee_id,)).fetchone()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="An employee with this email already exists")

@app.delete("/api/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int):
    with connect() as db:
        cur = db.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
