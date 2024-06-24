from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_sucursal(sucursal: schemas.sucursales, db: Session):
    db= SessionLocal()
    nueva_sucursal= models.Sucursales(**sucursal.model_dump())
    db.add(nueva_sucursal)
    db.commit()
    db.refresh(nueva_sucursal)
    return nueva_sucursal

def get_sucursales(db:Session):
    db=SessionLocal()
    return db.query(models.Sucursales).all()

def get_sucursal(id:int, db:Session):
    db=SessionLocal()
    return db.query(models.Sucursales).filter(models.Sucursales.id==id).first()

def update_sucursal(id:int, sucursal:schemas.sucursalUpdate, db:Session):
    db= SessionLocal()
    data=db.query(models.Sucursales).filter(models.Sucursales.id==id).first()
    data.nombre = sucursal.nombre
    data.direccion=sucursal.direccion
    db.commit()
    return data

def delete_sucursal(id:int, db:Session):
    db=SessionLocal()
    data=db.query(models.Sucursales).filter(models.Sucursales.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    