from fastapi import APIRouter, Depends
from app.database import SessionLocal
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.ordenes import models, schemas
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerOrdenes=APIRouter(
    tags=["Ordenes"],
    prefix="/ordenes",
    dependencies=[Depends(seguridad)]
    )


@routerOrdenes.get('/')
async def get_ordenes(db: Session = Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Ordenes).all()
    return data

@routerOrdenes.get('/{id}')
async def get_orden(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Ordenes).filter(models.Ordenes.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerOrdenes.post('/')
async def create_orden(ordenes: schemas.ordenes, db: Session=Depends(get_db)):
    db= SessionLocal()
    nueva_orden= models.Ordenes(**ordenes.model_dump())
    db.add(nueva_orden)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva orden','orden': ordenes.model_dump()})

@routerOrdenes.put('/{id}')
async def update_ordenes(id:int, ordenes:schemas.ordenes, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Ordenes).filter(models.Ordenes.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró orden'})
    
    data.nombre = ordenes.nombre
    data.email= ordenes.email
    db.commit()
    return JSONResponse(status_code=200, content={'message':'se modificó la orden'})

@routerOrdenes.delete('/{id}')
async def delete_usuario(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Ordenes).filter(models.Ordenes.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró la orden'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message':'se ha eliminado una orden','orden':jsonable_encoder(data)})