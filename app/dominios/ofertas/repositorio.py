from sqlalchemy.orm import Session
from . import models, schemas
from ...database import SessionLocal

def create_oferta(oferta: schemas.oferta, db: Session):
    
    nueva_oferta= models.Ofertas(**oferta.model_dump())
    db.add(nueva_oferta)
    db.commit()
    db.refresh(nueva_oferta)
    return nueva_oferta

def get_ofertas(db:Session):
    
    return db.query(models.Ofertas).all()

def get_oferta(id:int, db:Session):
    
    return db.query(models.Ofertas).filter(models.Ofertas.id==id).first()

def update_oferta(id:int, oferta:schemas.ofertaUpdate, db:Session):
    
    data=db.query(models.Ofertas).filter(models.Ofertas.id==id).first()
    data.descuento = oferta.descuento
    data.fecha_inicio = oferta.fecha_inicio
    data.fecha_fin = oferta.fecha_fin
    data.sucursal_id = oferta.sucursal_id
    data.producto_id = oferta.producto_id
    db.commit()
    return data

def delete_oferta(id:int, db:Session):
    
    data=db.query(models.Ofertas).filter(models.Ofertas.id==id).first()
    db.delete(data)
    db.commit()
    return print("se elimino correctamente")    