from typing import Annotated

from fastapi import (
    Depends,
    FastAPI,
    Query,
)
from pydantic import BaseModel
from sqlmodel import (
    create_engine,
    select,
    Session,
    SQLModel,
)

from models import Hero


sqlite_file_name = 'db.sqlite3'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session



SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db_and_tables()


@app.get("/heroes/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(
        select(Hero).offset(offset).limit(limit)
    ).all()
    return heroes
