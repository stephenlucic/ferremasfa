from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import relationship
from ...database import Base

class Ordenes(Base):
    __tablename__='orden_compra'
    id=Column(Integer, primary_key=True)
    fecha_orden=Column(String)
    usuario_id= Column(Integer)
    estado= Column(String)