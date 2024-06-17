from fastapi import APIRouter, Depends
from app.database import SessionLocal
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.usuarios import models
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



routerUsuario=APIRouter(
    tags=["Usuarios"],
    prefix="/usuarios"
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


