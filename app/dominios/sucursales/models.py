from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Sucursales(Base):
    __tablename__='sucursal'
    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    direccion=Column(String)