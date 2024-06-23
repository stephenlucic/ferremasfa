from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.usuarios import schemas,servicio
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
    data=servicio.get_usuarios(db)
    return data

@routerUsuario.get('/{id}')
async def get_usuario(id:int, db: Session=Depends(get_db)):
    data= servicio.get_usuario(id, db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerUsuario.post('/')
async def create_usuario(usuario: schemas.usuario, db: Session=Depends(get_db)):
    servicio.create_usuario(usuario, db)
    return  JSONResponse(status_code=201, content={'message':'Se ha creado el usuario','usuario': usuario.model_dump()})

@routerUsuario.put('/{id}')
async def update_usuario(id:int, usuario:schemas.usuarioUpdate, db: Session=Depends(get_db)):
    data=servicio.get_usuario(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el usuario'})
    servicio.update_usuario(id,usuario,db)
    data=servicio.get_usuario(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó el usuario','usuario': jsonable_encoder(data)})

@routerUsuario.delete('/{id}')
async def delete_usuario(id:int, db: Session=Depends(get_db)):
    data=servicio.get_usuario(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el usuario'})
    servicio.delete_usuario(id,db)
    return JSONResponse(content={'message':'se ha eliminado un usuario','usuario':jsonable_encoder(data)})