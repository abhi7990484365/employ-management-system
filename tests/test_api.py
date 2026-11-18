def payload(name="Alex Morgan", email="alex@example.com", department="Engineering"):
    return {"name": name, "email": email, "department": department}

def test_create_and_list(client):
    created = client.post("/api/employees", json=payload())
    assert created.status_code == 201
    assert created.json()["name"] == "Alex Morgan"
    assert len(client.get("/api/employees").json()) == 1

def test_duplicate_email_rejected(client):
    assert client.post("/api/employees", json=payload()).status_code == 201
    assert client.post("/api/employees", json=payload(name="Alex Two")).status_code == 409

def test_update_and_delete(client):
    employee_id = client.post("/api/employees", json=payload()).json()["id"]
    updated = client.put(f"/api/employees/{employee_id}", json=payload(department="QA"))
    assert updated.status_code == 200
    assert updated.json()["department"] == "QA"
    assert client.delete(f"/api/employees/{employee_id}").status_code == 204

def test_missing_employee_returns_404(client):
    assert client.delete("/api/employees/999").status_code == 404

def test_search(client):
    client.post("/api/employees", json=payload())
    client.post("/api/employees", json=payload("Sam Lee", "sam@example.com", "Finance"))
    result = client.get("/api/employees?search=Alex").json()
    assert len(result) == 1 and result[0]["name"] == "Alex Morgan"
