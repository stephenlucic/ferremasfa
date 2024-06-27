from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Ventas(Base):
    __tablename__='ventas'
    id=Column(Integer, primary_key=True)
    fecha_emision=Column(String)
    cantidad= Column(Integer)
    monto= Column(Float)
    producto_id=Column(Integer)
    orden_id=Column(Integer)