from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from ...database import Base

class Inventarios(Base):
    __tablename__='inventario'
    id=Column(Integer, primary_key=True)
    cantidad= Column(Integer)
    sucursal_id=Column(Integer)
    producto_id= Column(Integer)
    