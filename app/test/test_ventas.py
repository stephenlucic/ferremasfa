import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ventas import models, schemas
from ..dominios.ventas.repositorio import create_ventas,get_venta,get_ventas,update_venta,delete_venta

# Configurar la base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de datos y las tablas
models.Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db() -> Session:
    # Crear una sesión de base de datos para pruebas
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_venta(db):
    venta = schemas.ventas(id=1, fecha_emision="12 de junio", cantidad=23, monto=43999, producto_id=1, orden_id=1)
    venta_creada = create_ventas(venta, db)
    assert venta_creada.id == 1
    assert venta_creada.fecha_emision == "12 de junio"
    assert venta_creada.cantidad == 23
    assert venta_creada.monto == 43999
    assert venta_creada.producto_id == 1
    assert venta_creada.orden_id == 1

def test_get_venta(db):
    venta = schemas.ventas(id=2, fecha_emision="12 de junio", cantidad=23, monto=43999, producto_id=2, orden_id=2)
    venta_creada = create_ventas(venta, db)
    obtener_venta = get_venta(venta_creada.id,db)
    assert obtener_venta
    assert obtener_venta.id == 2

def test_update_venta(db):
    venta = schemas.ventas(id=4,fecha_emision= "24/12/2023",cantidad=3000,monto=500000,producto_id= 5,orden_id= 5)
    venta_creada = create_ventas(venta, db)
    nueva_venta = schemas.ventasUpdate(fecha_emision= "21/10/2024",cantidad=10,monto=500,producto_id= 6,orden_id= 6)
    venta_actualizada = update_venta(venta_creada.id, nueva_venta, db)
    assert venta_actualizada
    assert venta_actualizada.id == venta_creada.id
    assert venta_actualizada.fecha_emision == nueva_venta.fecha_emision
    assert venta_actualizada.cantidad == nueva_venta.cantidad
    assert venta_actualizada.monto == nueva_venta.monto
    assert venta_actualizada.producto_id == nueva_venta.producto_id
    assert venta_actualizada.orden_id == nueva_venta.orden_id
    
    
def test_get_ventas(db):
    obtener_venta = get_ventas(db)   
    assert obtener_venta
    assert obtener_venta == db.query(models.Ventas).all()
    
def test_delete_venta(db):
    borrar_venta = delete_venta(2,db)
    assert borrar_venta is None  
    
    venta_eliminada = db.query(models.Ventas).filter(models.Ventas.id == 2).first()
    assert venta_eliminada is None       