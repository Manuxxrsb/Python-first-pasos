from sqlalchemy import Boolean , Column , ForeignKey , Integer , String
from database import Base


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer,primary_key=True,index=True)
    item_nombre = Column(String,index=True)
    dueno_id = Column(Integer,ForeignKey("persona.id"))

class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String,index=True)