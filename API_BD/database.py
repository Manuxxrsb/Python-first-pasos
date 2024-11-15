from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "postgresql://postgres:1234567@localhost:5432/sisdeinfo"

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()