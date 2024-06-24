from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.ventas import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerVentas=APIRouter(
    tags=["Ventas"],
    prefix="/ventas",
    dependencies=[Depends(seguridad)]
    )


@routerVentas.get('/')
async def get_ventas(db: Session = Depends(get_db)):
    data=servicio.get_ventas(db)
    return data

@routerVentas.get('/{id}')
async def get_venta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_venta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'venta no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerVentas.post('/')
async def create_venta(venta: schemas.ventas, db: Session=Depends(get_db)):
    servicio.create_venta(venta,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva venta','venta': venta.model_dump()})

@routerVentas.put('/{id}')
async def update_venta(id:int, venta:schemas.ventasUpdate, db: Session=Depends(get_db)):
    data=servicio.get_venta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró venta'})
    servicio.update_venta(id,venta,db)
    data=servicio.get_venta(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó venta','venta':jsonable_encoder(data)})

@routerVentas.delete('/{id}')
async def delete_venta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_venta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró venta'})
    servicio.delete_venta(id,db)
    return JSONResponse(content={'message':'se ha eliminado venta','venta':jsonable_encoder(data)})