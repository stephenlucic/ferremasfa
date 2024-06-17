from fastapi import APIRouter, Depends
from app.database import SessionLocal
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.usuarios import models, schemas
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerUsuario=APIRouter(
    tags=["Usuarios"],
    prefix="/usuarios",
    dependencies=[Depends(seguridad)]
    )


@routerUsuario.get('/')
async def get_usuarios(db: Session = Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Usuario).all()
    return data

@routerUsuario.get('/{id}')
async def get_usuario(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerUsuario.post('/')
async def create_usuario(usuario: schemas.usuario, db: Session=Depends(get_db)):
    db= SessionLocal()
    nuevo_usuario= models.Usuario(**usuario.model_dump())
    db.add(nuevo_usuario)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha creado el usuario','usuario': usuario.model_dump()})

@routerUsuario.put('/{id}')
async def update_usuario(id:int, usuario:schemas.usuario, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el usuario'})
    
    data.nombre = usuario.nombre
    data.email= usuario.email
    db.commit()
    return JSONResponse(status_code=200, content={'message':'se modificó el usuario'})

@routerUsuario.delete('/{id}')
async def delete_usuario(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Usuario).filter(models.Usuario.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el usuario'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message':'se ha eliminado un usuario','usuario':jsonable_encoder(data)})