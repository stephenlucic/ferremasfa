from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.inventarios import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerInventario=APIRouter(
    tags=["Inventario"],
    prefix="/inventario",
    dependencies=[Depends(seguridad)]
    )


@routerInventario.get('/')
async def get_inventario(db: Session = Depends(get_db)):
    data=servicio.get_inventarios(db)
    return data

@routerInventario.get('/{id}')
async def get_inventario(id:int, db: Session=Depends(get_db)):
    data=servicio.get_inventario(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'inventario no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerInventario.post('/')
async def create_inventario(inventario: schemas.inventarios, db: Session=Depends(get_db)):
    servicio.create_inventario(inventario,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nuevo inventario','inventario': inventario.model_dump()})

@routerInventario.put('/{id}')
async def update_inventario(id:int, inventario:schemas.inventarioUpdate, db: Session=Depends(get_db)):
    data=servicio.get_inventario(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró inventario'})
    servicio.update_inventario(id,inventario,db)
    data=servicio.get_inventario(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó inventario','inventario':jsonable_encoder(data)})

@routerInventario.delete('/{id}')
async def delete_inventario(id:int, db: Session=Depends(get_db)):
    data=servicio.get_inventario(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró inventario'})
    servicio.delete_inventario(id,db)
    return JSONResponse(content={'message':'se ha eliminado inventario','inventario':jsonable_encoder(data)})