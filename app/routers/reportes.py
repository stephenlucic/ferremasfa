from fastapi import APIRouter, Depends
from ..dependencias import get_db
from sqlalchemy.orm import Session
from ..dominios.reportes import schemas,servicio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .auth import seguridad



routerReporte=APIRouter(
    tags=["Reportes"],
    prefix="/reportes",
    dependencies=[Depends(seguridad)]
    )


@routerReporte.get('/')
async def get_reportes(db: Session = Depends(get_db)):
    data=servicio.get_reportes(db)
    return data

@routerReporte.get('/{id}')
async def get_reporte(id:int, db: Session=Depends(get_db)):
    data=servicio.get_reporte(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'reporte no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerReporte.post('/')
async def create_reporte(reporte: schemas.reportes, db: Session=Depends(get_db)):
    servicio.create_reporte(reporte,db)
    return JSONResponse(status_code=201, content={'message':'Se ha creado nuevo reporte','reporte': reporte.model_dump()})

@routerReporte.put('/{id}')
async def update_reporte(id:int, reporte:schemas.reportesUpdate, db: Session=Depends(get_db)):
    data=servicio.get_reporte(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró reporte'})
    servicio.update_reporte(id,reporte,db)
    data=servicio.get_reporte(id,db)
    return JSONResponse(status_code=200, content={'message':'se modificó el reporte','reporte':jsonable_encoder(data)})

@routerReporte.delete('/{id}')
async def delete_reporte(id:int, db: Session=Depends(get_db)):
    data=servicio.get_reporte(id,db)
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró el reporte'})
    servicio.delete_reporte(id,db)
    return JSONResponse(content={'message':'se ha eliminado un reporte','reporte':jsonable_encoder(data)})