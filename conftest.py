import pytest
from app import create_app
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dependency_injector.wiring import Provide

@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    db = app.container.db()
    db.create_database()
    return app

@pytest.fixture
def test_client() -> TestClient:
    app = create_app()
    db = app.container.db()
    db.create_database()
    return TestClient(app)

