from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_oferta(oferta:schemas.oferta, db:Session):
    return repositorio.create_oferta(db=db,oferta=oferta)

def get_ofertas(db:Session):
    return repositorio.get_ofertas(db=db)

def get_oferta(id:int, db:Session):
    return repositorio.get_oferta(id=id, db=db)

def update_oferta(id:int, oferta:schemas.ofertaUpdate, db:Session):
    return repositorio.update_oferta(id=id,oferta=oferta,db=db)

def delete_oferta(id:int, db:Session):
    return repositorio.delete_oferta(id=id,db=db)