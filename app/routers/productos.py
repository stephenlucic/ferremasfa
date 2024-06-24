from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.productos import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerProducto=APIRouter(
    tags=["Productos"],
    prefix="/productos",
    dependencies=[Depends(seguridad)]
    )


@routerProducto.get('/')
async def get_productos(db: Session = Depends(get_db)):
    data=servicio.get_productos(db)
    return data

@routerProducto.get('/{id}')
async def get_producto(id:int, db: Session=Depends(get_db)):
    data=servicio.get_producto(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'producto no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerProducto.post('/')
async def create_producto(producto: schemas.productos, db: Session=Depends(get_db)):
    servicio.create_producto(producto,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nuevo producto','producto': producto.model_dump()})

@routerProducto.put('/{id}')
async def update_producto(id:int, producto:schemas.productos, db: Session=Depends(get_db)):
    data=servicio.get_producto(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró producto'})
    servicio.update_producto(id,producto,db)
    data=servicio.get_producto(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó el producto','producto':jsonable_encoder(data)})

@routerProducto.delete('/{id}')
async def delete_producto(id:int, db: Session=Depends(get_db)):
    data=servicio.get_producto(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el producto'})
    servicio.delete_producto(id,db)
    return JSONResponse(content={'message':'se ha eliminado un producto','producto':jsonable_encoder(data)})