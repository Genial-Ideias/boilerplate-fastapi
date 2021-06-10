import os
import pytest
from app import create_app
from fastapi import FastAPI
from fastapi.testclient import TestClient

@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    db = app.container.db()
    db.create_database()
    try:
        yield app
    finally:
        if os.path.exists("test.db"):
            os.remove('test.db')


@pytest.fixture
def test_client() -> TestClient:
    app = create_app()
    db = app.container.db()
    db.create_database()
    try:
        yield TestClient(app)
    finally:
        if os.path.exists("test.db"):
            os.remove('test.db')


if os.path.exists("test.db"):
    os.remove('test.db')
