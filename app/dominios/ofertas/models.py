from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Ofertas(Base):
    __tablename__='oferta'
    id=Column(Integer, primary_key=True)
    descuento= Column(Float)
    fecha_inicio= Column(String)
    fecha_fin= Column(String)
    sucursal_id= Column(Integer)
    producto_id= Column(Integer)