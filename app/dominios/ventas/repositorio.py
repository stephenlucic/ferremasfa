from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_ventas(venta: schemas.ventas, db: Session):
    
    nueva_venta= models.Ventas(**venta.model_dump())
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def get_ventas(db:Session):
    
    return db.query(models.Ventas).all()

def get_venta(id:int, db:Session):
    
    return db.query(models.Ventas).filter(models.Ventas.id==id).first()

def update_venta(id:int, venta:schemas.ventasUpdate, db:Session):
    
    data=db.query(models.Ventas).filter(models.Ventas.id==id).first()
    data.fecha_emision = venta.fecha_emision
    data.cantidad=venta.cantidad
    data.monto = venta.monto
    data.producto_id= venta.producto_id
    data.orden_id=venta.orden_id
    db.commit()
    return data

def delete_venta(id:int, db:Session):
    
    data=db.query(models.Ventas).filter(models.Ventas.id==id).first()
    db.delete(data)
    db.commit()
    return 