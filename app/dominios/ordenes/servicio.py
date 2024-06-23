from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_orden(orden:schemas.ordenes, db:Session):
    return repositorio.create_orden(db=db,orden=orden)

def get_ordenes(db:Session):
    return repositorio.get_ordenes(db=db)

def get_orden(id:int, db:Session):
    return repositorio.get_orden(id=id, db=db)

def update_orden(id:int, orden:schemas.ordenes, db:Session):
    return repositorio.update_orden(id=id,orden=orden,db=db)

def delete_orden(id:int, db:Session):
    return repositorio.delete_orden(id=id,db=db)