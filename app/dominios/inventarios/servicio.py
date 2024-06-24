from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_inventario(inventario:schemas.inventarios, db:Session):
    return repositorio.create_inventario(db=db,inventario=inventario)

def get_inventarios(db:Session):
    return repositorio.get_inventarios(db=db)

def get_inventario(id:int, db:Session):
    return repositorio.get_inventario(id=id, db=db)

def update_inventario(id:int, inventario:schemas.inventarioUpdate, db:Session):
    return repositorio.update_inventario(id=id,inventario=inventario,db=db)

def delete_inventario(id:int, db:Session):
    return repositorio.delete_inventario(id=id,db=db)