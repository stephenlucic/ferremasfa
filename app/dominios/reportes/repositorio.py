from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_reporte(reporte: schemas.reportes, db: Session):
    
    nuevo_reporte= models.Reportes(**reporte.model_dump())
    db.add(nuevo_reporte)
    db.commit()
    db.refresh(nuevo_reporte)
    return nuevo_reporte

def get_reportes(db:Session):
    
    return db.query(models.Reportes).all()

def get_reporte(id:int, db:Session):
    
    return db.query(models.Reportes).filter(models.Reportes.id==id).first()

def update_reporte(id:int, reporte:schemas.reportesUpdate, db:Session):
    
    data=db.query(models.Reportes).filter(models.Reportes.id==id).first()
    data.usuario_id=reporte.usuario_id
    data.tipo = reporte.tipo
    data.fecha_generada = reporte.fecha_generada
    db.commit()
    return data

def delete_reporte(id:int, db:Session):
    
    data=db.query(models.Reportes).filter(models.Reportes.id==id).first()
    db.delete(data)
    db.commit()
    return   