from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_boleta(boleta:schemas.boletas, db:Session):
    return repositorio.create_boleta(db=db,boleta=boleta)

def get_boletas(db:Session):
    return repositorio.get_boletas(db=db)

def get_boleta(id:int, db:Session):
    return repositorio.get_boleta(id=id, db=db)

def update_boleta(id:int, boleta:schemas.boletaUpdate, db:Session):
    return repositorio.update_boleta(id=id,boleta=boleta,db=db)

def delete_boleta(id:int, db:Session):
    return repositorio.delete_boleta(id=id,db=db)