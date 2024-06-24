from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_sucursal(sucursal:schemas.sucursales, db:Session):
    return repositorio.create_sucursal(db=db,sucursal=sucursal)

def get_sucursales(db:Session):
    return repositorio.get_sucursales(db=db)

def get_sucursal(id:int, db:Session):
    return repositorio.get_sucursal(id=id, db=db)

def update_sucursal(id:int, sucursal:schemas.sucursalUpdate, db:Session):
    return repositorio.update_sucursal(id=id,sucursal=sucursal,db=db)

def delete_sucursal(id:int, db:Session):
    return repositorio.delete_sucursal(id=id,db=db)