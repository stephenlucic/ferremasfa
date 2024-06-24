from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Productos(Base):
    __tablename__='producto'
    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    descripcion= Column(String)
    precio= Column(Float)
    categoria=Column(String)