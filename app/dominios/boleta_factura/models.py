from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Boletas_Facturas(Base):
    __tablename__='boleta_factura'
    id=Column(Integer, primary_key=True)
    orden_id=Column(Integer)
    fecha_emision= Column(String)
    monto_total= Column(Float)
    cantidad= Column(Integer)