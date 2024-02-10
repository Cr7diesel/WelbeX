import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Routes(Base):

    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)
