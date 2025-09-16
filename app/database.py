from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.settings import settings



DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

Sessionmaker = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionmaker()
    try:
        yield db
    finally:
        db.close()

