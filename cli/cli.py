from sqlalchemy import create_engine
from app.models.base import Base


def create_tables():
    engine = create_engine("sqlite:///./db/library.db")
    Base.metadata.create_all(engine)
    print("Tables created (if not already existing)")

if __name__ == "__main__":
    create_tables()
