from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_NAME = Path(__file__).resolve().parent.parent / "students.db"

engine = create_engine(f"sqlite:///{DATABASE_NAME.as_posix()}")
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
