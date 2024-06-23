from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal


def create_usuario(usuario: schemas.usuario, db: Session):
    db= SessionLocal()
    nuevo_usuario= models.Usuario(**usuario.model_dump())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def get_usuarios(db:Session):
    db=SessionLocal()
    return db.query(models.Usuario).all()

def get_usuario(id:int, db:Session):
    db=SessionLocal()
    return db.query(models.Usuario).filter(models.Usuario.id==id).first()

def update_usuario(id:int, usuario:schemas.usuarioUpdate, db:Session):
    db= SessionLocal()
    data=db.query(models.Usuario).filter(models.Usuario.id==id).first()
    data.nombre = usuario.nombre
    data.apellidos=usuario.apellidos
    data.email = usuario.email
    data.direccion=usuario.direccion
    db.commit()
    return data

def delete_usuario(id:int, db:Session):
    db=SessionLocal()
    data=db.query(models.Usuario).filter(models.Usuario.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    
