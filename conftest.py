import os
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from typer import Typer

from app import create_app
from cli import create_app as create_test_app

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

@pytest.fixture
def cli_app() -> Typer:
    app = create_test_app()
    db = app.container.db()
    db.create_database()
    try:
        yield app
    finally:
        if os.path.exists("test.db"):
            os.remove('test.db')

if os.path.exists("test.db"):
    os.remove('test.db')
