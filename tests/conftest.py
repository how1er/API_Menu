from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db import Base, get_db
from main import app

from app.config import settings
import pytest
from fastapi.testclient import TestClient

from app.routers import crud
from app import schemas


client = TestClient(app)


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_TEST}:{settings.DATABASE_PORT}/{settings.POSTGRES_TESTDB}"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()

    # begin a non-ORM transaction
    connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection)
    # db = Session(db_engine)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app=app) as c:
        yield c


@pytest.fixture
def create_menu(db, menu):
    def create_menu(db, menu):
        crud.create_menu(
            schemas.CreateMenu(
                title=menu["title"], description=menu["description"]), db
        )

    return create_menu


@pytest.fixture
def create_menu_list(db):
    crud.create_menu(
        schemas.CreateMenu(title="title 1", description="description 1"), db
    )
    crud.create_menu(
        schemas.CreateMenu(title="title 2", description="description 2"), db
    )
    crud.create_menu(
        schemas.CreateMenu(title="title 3", description="description 3"), db
    )


@pytest.fixture
def create_submenu(db, submenu):
    def create_submenu(db, submenu):
        crud.create_menu(
            schemas.CreateSubMenu(
                title=submenu["title"], description=submenu["description"]
            ),
            db,
        )

    return create_submenu


@pytest.fixture
def dish():
    return {
        "title": "Test dish",
        "price": "14.5",
        "description": "Test dish description",
    }


@pytest.fixture
def submenu():
    return {"title": "Test submenu", "description": "Test submenu description"}


@pytest.fixture
def menu():
    return {"title": "Test menu", "description": "Test menu description"}
