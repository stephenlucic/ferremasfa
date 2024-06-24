from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.sucursales import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerSucursales=APIRouter(
    tags=["Sucursales"],
    prefix="/sucursal",
    dependencies=[Depends(seguridad)]
    )


@routerSucursales.get('/')
async def get_sucursales(db: Session = Depends(get_db)):
    data=servicio.get_sucursales(db)
    return data

@routerSucursales.get('/{id}')
async def get_sucursal(id:int, db: Session=Depends(get_db)):
    data=servicio.get_sucursal(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'sucursal no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerSucursales.post('/')
async def create_sucursal(sucursal: schemas.sucursales, db: Session=Depends(get_db)):
    servicio.create_sucursal(sucursal,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva sucursal','sucursal': sucursal.model_dump()})

@routerSucursales.put('/{id}')
async def update_sucursal(id:int, sucursal:schemas.sucursalUpdate, db: Session=Depends(get_db)):
    data=servicio.get_sucursal(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró sucursal'})
    servicio.update_sucursal(id,sucursal,db)
    data=servicio.get_sucursal(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó sucursal','sucursal':jsonable_encoder(data)})

@routerSucursales.delete('/{id}')
async def delete_sucursal(id:int, db: Session=Depends(get_db)):
    data=servicio.get_sucursal(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró sucursal'})
    servicio.delete_sucursal(id,db)
    return JSONResponse(content={'message':'se ha eliminado sucursal','sucursal':jsonable_encoder(data)})