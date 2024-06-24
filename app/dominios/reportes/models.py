from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from ...database import Base

class Reportes(Base):
    __tablename__='reporte'
    id=Column(Integer, primary_key=True)
    usuario_id= Column(Integer)
    tipo=Column(String)
    fecha_generada= Column(String)