from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_venta(venta:schemas.ventas, db:Session):
    return repositorio.create_ventas(db=db,venta=venta)

def get_ventas(db:Session):
    return repositorio.get_ventas(db=db)

def get_venta(id:int, db:Session):
    return repositorio.get_venta(id=id, db=db)

def update_venta(id:int, venta:schemas.ventasUpdate, db:Session):
    return repositorio.update_venta(id=id,venta=venta,db=db)

def delete_venta(id:int, db:Session):
    return repositorio.delete_venta(id=id,db=db)