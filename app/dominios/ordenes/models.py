from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Ordenes(Base):
    __tablename__='ordenes'
    id=Column(Integer, primary_key=True)
    detalle=Column(String)
    usuario_id= Column(Integer)
    producto_id= Column(Integer)