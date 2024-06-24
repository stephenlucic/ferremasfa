from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_reporte(reporte:schemas.reportes, db:Session):
    return repositorio.create_reporte(db=db,reporte=reporte)

def get_reportes(db:Session):
    return repositorio.get_reportes(db=db)

def get_reporte(id:int, db:Session):
    return repositorio.get_reporte(id=id, db=db)

def update_reporte(id:int, reporte:schemas.reportesUpdate, db:Session):
    return repositorio.update_reporte(id=id,reporte=reporte,db=db)

def delete_reporte(id:int, db:Session):
    return repositorio.delete_reporte(id=id,db=db)