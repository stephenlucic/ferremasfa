from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_orden(orden: schemas.ordenes, db: Session):
    
    nueva_orden= models.Ordenes(**orden.model_dump())
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden

def get_ordenes(db:Session):
    
    return db.query(models.Ordenes).all()

def get_orden(id:int, db:Session):
    
    return db.query(models.Ordenes).filter(models.Ordenes.id==id).first()

def update_orden(id:int, orden:schemas.ordenesUpdate, db:Session):
    
    data=db.query(models.Ordenes).filter(models.Ordenes.id==id).first()
    data.fecha_orden = orden.fecha_orden
    data.usuario_id=orden.usuario_id
    data.estado = orden.estado
    db.commit()
    return data

def delete_orden(id:int, db:Session):
    
    data=db.query(models.Ordenes).filter(models.Ordenes.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    