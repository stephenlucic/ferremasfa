from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.ordenes import schemas,servicio
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
    data=servicio.get_ordenes(db)
    return data

@routerOrdenes.get('/{id}')
async def get_orden(id:int, db: Session=Depends(get_db)):
    data=servicio.get_orden(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'orden no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerOrdenes.post('/')
async def create_orden(orden: schemas.ordenes, db: Session=Depends(get_db)):
    servicio.create_orden(orden,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva orden','orden': orden.model_dump()})

@routerOrdenes.put('/{id}')
async def update_orden(id:int, orden:schemas.ordenes, db: Session=Depends(get_db)):
    data=servicio.get_orden(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró orden'})
    servicio.update_orden(id,orden,db)
    data=servicio.get_orden(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó orden','orden':jsonable_encoder(data)})

@routerOrdenes.delete('/{id}')
async def delete_orden(id:int, db: Session=Depends(get_db)):
    data=servicio.get_orden(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró orden'})
    servicio.delete_orden(id,db)
    return JSONResponse(content={'message':'se ha eliminado orden','orden':jsonable_encoder(data)})