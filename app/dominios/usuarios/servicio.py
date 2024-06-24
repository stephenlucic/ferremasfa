from sqlalchemy.orm import Session
from . import repositorio,schemas

def create_usuario(usuario:schemas.usuario, db:Session):
    return repositorio.create_usuario(db=db,usuario=usuario)

def get_usuarios(db:Session):
    return repositorio.get_usuarios(db=db)

def get_usuario(id:int, db:Session):
    return repositorio.get_usuario(id=id, db=db)

def update_usuario(id:int, usuario:schemas.usuarioUpdate, db:Session):
    return repositorio.update_usuario(id=id,usuario=usuario,db=db)

def delete_usuario(id:int, db:Session):
    return repositorio.delete_usuario(id=id,db=db)