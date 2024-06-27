from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_boleta(boleta: schemas.boletas, db: Session):
   
    nueva_boleta= models.Boletas_Facturas(**boleta.model_dump())
    db.add(nueva_boleta)
    db.commit()
    db.refresh(nueva_boleta)
    return nueva_boleta

def get_boletas(db:Session):

    return db.query(models.Boletas_Facturas).all()

def get_boleta(id:int, db:Session):
    
    return db.query(models.Boletas_Facturas).filter(models.Boletas_Facturas.id==id).first()

def update_boleta(id:int, boleta:schemas.boletaUpdate, db:Session):
   
    data=db.query(models.Boletas_Facturas).filter(models.Boletas_Facturas.id==id).first()
    data.orden_id = boleta.orden_id
    data.fecha_emision=boleta.fecha_emision
    data.monto_total = boleta.monto_total
    data.cantidad = boleta.cantidad
    db.commit()
    return data

def delete_boleta(id:int, db:Session):
    
    data=db.query(models.Boletas_Facturas).filter(models.Boletas_Facturas.id==id).first()
    db.delete(data)
    db.commit()
    return 