from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Usuario(Base):
    __tablename__='usuario'
    id=Column(Integer, primary_key=True)
    nombre= Column(String)
    apellidos=Column(String)
    email= Column(String)
    direccion=Column(String)


