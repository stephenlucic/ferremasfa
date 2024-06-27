from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_producto(producto: schemas.productos, db: Session):
    
    nuevo_producto= models.Productos(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def get_productos(db:Session):
  
    return db.query(models.Productos).all()

def get_producto(id:int, db:Session):
 
    return db.query(models.Productos).filter(models.Productos.id==id).first()

def update_producto(id:int, producto:schemas.productoUpdate, db:Session):
   
    data=db.query(models.Productos).filter(models.Productos.id==id).first()
    data.nombre = producto.nombre
    data.descripcion=producto.descripcion
    data.precio = producto.precio
    data.categoria=producto.categoria
    db.commit()
    return data

def delete_producto(id:int, db:Session):
  
    data=db.query(models.Productos).filter(models.Productos.id==id).first()
    db.delete(data)
    db.commit()
    return 