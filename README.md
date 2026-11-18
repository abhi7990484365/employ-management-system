# Employee Management System

A GitHub-ready mini project for testing an AI-driven SDLC workflow.

## Stack
Python, FastAPI, SQLite, HTML/CSS/JavaScript, Pytest, Playwright.

## Features
- Add, view, update and delete employees
- Search employees by name
- Required-field validation
- Reject duplicate email addresses
- SQLite persistence
- Delete asks for browser confirmation ("Delete this employee?") before removing

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000. API docs: http://127.0.0.1:8000/docs

## Run API tests
```bash
pytest tests/test_api.py -v
```

## Run UI tests
Keep the app running in another terminal:
```bash
playwright install chromium
pytest tests/test_ui.py -v
```

UI tests use the real `employees.db` and are not run in CI. See `docs/test-plan.md` and `docs/status.md` for limitations.

## Suggested Jira story
**EMP-101 – Employee CRUD Management**

As an administrator, I want to add, view, update, delete and search employees so that I can manage employee information.

Acceptance criteria:
1. Create employees with name, email and department.
2. Persist records in SQLite.
3. List, update and delete employees.
4. Reject duplicate email addresses.
5. Validate required fields.
6. Search employees by name.

## Push to GitHub
Create a repository named `employee-management-system`, then:
```bash
git init
git add .
git commit -m "Initial employee management system"
git branch -M main
git remote add origin https://github.com/<your-username>/employee-management-system.git
git push -u origin main
```
