from sqlalchemy import create_engine
from app.models.base import Base


if __name__ == "__main__":
   engine = create_engine("sqlite:///./app/db/library.db")
   Base.metadata.create_all(engine)


print("Tables created (if not already existing)")