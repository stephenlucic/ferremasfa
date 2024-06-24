from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.ofertas import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerOfertas=APIRouter(
    tags=["Ofertas"],
    prefix="/oferta",
    dependencies=[Depends(seguridad)]
    )


@routerOfertas.get('/')
async def get_ofertas(db: Session = Depends(get_db)):
    data=servicio.get_ofertas(db)
    return data

@routerOfertas.get('/{id}')
async def get_oferta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_oferta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'oferta no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerOfertas.post('/')
async def create_oferta(oferta: schemas.oferta, db: Session=Depends(get_db)):
    servicio.create_oferta(oferta,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nueva oferta','oferta': oferta.model_dump()})

@routerOfertas.put('/{id}')
async def update_oferta(id:int, oferta:schemas.ofertaUpdate, db: Session=Depends(get_db)):
    data=servicio.get_oferta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró oferta'})
    servicio.update_oferta(id,oferta,db)
    data=servicio.get_oferta(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó oferta','oferta':jsonable_encoder(data)})

@routerOfertas.delete('/{id}')
async def delete_oferta(id:int, db: Session=Depends(get_db)):
    data=servicio.get_oferta(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró oferta'})
    servicio.delete_oferta(id,db)
    return JSONResponse(content={'message':'se ha eliminado oferta','oferta':jsonable_encoder(data)})