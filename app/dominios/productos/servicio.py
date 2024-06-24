from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_producto(producto:schemas.productos, db:Session):
    return repositorio.create_producto(db=db,producto=producto)

def get_productos(db:Session):
    return repositorio.get_productos(db=db)

def get_producto(id:int, db:Session):
    return repositorio.get_producto(id=id, db=db)

def update_producto(id:int, producto:schemas.productoUpdate, db:Session):
    return repositorio.update_producto(id=id,producto=producto,db=db)

def delete_producto(id:int, db:Session):
    return repositorio.delete_producto(id=id,db=db)