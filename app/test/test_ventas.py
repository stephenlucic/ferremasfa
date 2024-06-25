import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ventas import models, schemas
from ..dominios.ventas.repositorio import create_ventas,get_venta,get_ventas,update_venta,delete_venta
from ..dominios.ventas.servicio import create_ventas,get_venta,get_ventas,update_venta,delete_venta

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
    venta = schemas.ventas(id=3, fecha_emision="12 de junio", cantidad=23, monto=43999, producto_id=3, orden_id=3)
    venta_creada = create_ventas(venta, db)
    nueva_venta = schemas.ventasUpdate(nombre="Martillo grande", descripcion="Martillo grande de acero", precio=33000, categoria="herramientas")
    venta_actualizada = update_venta(venta_creada.id, nueva_venta, db)
    assert venta_actualizada
    assert venta_actualizada.id == venta_creada.id
    assert venta_actualizada.fecha_emision == nueva_venta.fecha_emision
    assert venta_actualizada.cantidad == nueva_venta.cantidad
    assert venta_actualizada.monto == nueva_venta.monto
    assert venta_actualizada.producto_id == nueva_venta.producto_id
    assert venta_actualizada.orden_id == nueva_venta.orden_id