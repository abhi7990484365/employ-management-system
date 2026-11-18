import os
import tempfile
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client(monkeypatch):
    from app import database
    from app.main import app
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    monkeypatch.setattr(database, "DB_PATH", path)
    with TestClient(app) as c:
        yield c
    os.unlink(path)
