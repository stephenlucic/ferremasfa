from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_inventario(inventario: schemas.inventarios, db: Session):
    
    nuevo_inventario= models.Inventarios(**inventario.model_dump())
    db.add(nuevo_inventario)
    db.commit()
    db.refresh(nuevo_inventario)
    return nuevo_inventario

def get_inventarios(db:Session):
    
    return db.query(models.Inventarios).all()

def get_inventario(id:int, db:Session):
    
    return db.query(models.Inventarios).filter(models.Inventarios.id==id).first()

def update_inventario(id:int, inventario:schemas.inventarioUpdate, db:Session):
    
    data=db.query(models.Inventarios).filter(models.Inventarios.id==id).first()
    data.cantidad = inventario.cantidad
    data.sucursal_id=inventario.sucursal_id
    data.producto_id = inventario.producto_id
    db.commit()
    return data

def delete_inventario(id:int, db:Session):
    
    data=db.query(models.Inventarios).filter(models.Inventarios.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    