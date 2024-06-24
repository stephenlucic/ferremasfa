from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_ventas(venta: schemas.ventas, db: Session):
    db= SessionLocal()
    nueva_venta= models.ventas(**venta.model_dump())
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def get_ventas(db:Session):
    db=SessionLocal()
    return db.query(models.ventas).all()

def get_venta(id:int, db:Session):
    db=SessionLocal()
    return db.query(models.ventas).filter(models.ventas.id==id).first()

def update_venta(id:int, venta:schemas.ventasUpdate, db:Session):
    db= SessionLocal()
    data=db.query(models.ventas).filter(models.ventas.id==id).first()
    data.fecha_emision = venta.fecha_emision
    data.cantidad=venta.cantidad
    data.monto = venta.monto
    data.producto_id= venta.producto_id
    data.orden_id=venta.orden_id
    db.commit()
    return data

def delete_venta(id:int, db:Session):
    db=SessionLocal()
    data=db.query(models.ventas).filter(models.ventas.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    