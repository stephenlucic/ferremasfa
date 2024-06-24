from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.boleta_factura import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerBoletas=APIRouter(
    tags=["Boletas y Facturas"],
    prefix="/boleta_factura",
    dependencies=[Depends(seguridad)]
    )


@routerBoletas.get('/')
async def get_boletas(db: Session = Depends(get_db)):
    data=servicio.get_boletas(db)
    return data

@routerBoletas.get('/{id}')
async def get_boleta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_boleta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'boleta no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerBoletas.post('/')
async def create_boleta(boleta: schemas.boletas, db: Session=Depends(get_db)):
    servicio.create_boleta(boleta,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva boleta','boleta': boleta.model_dump()})

@routerBoletas.put('/{id}')
async def update_boleta(id:int, boleta:schemas.boletaUpdate, db: Session=Depends(get_db)):
    data=servicio.get_boleta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró boleta'})
    servicio.update_boleta(id,boleta,db)
    data=servicio.get_boleta(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó boleta','boleta':jsonable_encoder(data)})

@routerBoletas.delete('/{id}')
async def delete_boleta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_boleta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró boleta'})
    servicio.delete_boleta(id,db)
    return JSONResponse(content={'message':'se ha eliminado boleta','boleta':jsonable_encoder(data)})