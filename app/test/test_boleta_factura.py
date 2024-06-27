import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.boleta_factura import models, schemas
from ..dominios.boleta_factura.repositorio import create_boleta,get_boleta,get_boletas,update_boleta,delete_boleta


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
    db = TestingSessionLocal()
    try:
        yield db
    finally:    
        models.Base.metadata.drop_all(bind=engine)
        db.close()

def test_create_boleta(db):
    boleta = schemas.boletas(id=1, orden_id=1, fecha_emision="23 de septiembre", monto_total=150000, cantidad=5)
    boleta_creada = create_boleta(boleta, db)
    assert boleta_creada.id == 1
    assert boleta_creada.orden_id == 1
    assert boleta_creada.fecha_emision == "23 de septiembre"
    assert boleta_creada.monto_total == 150000
    assert boleta_creada.cantidad == 5

def test_get_boleta(db):
    boleta = schemas.boletas(id=2,orden_id=2, fecha_emision="23 de septiembre", monto_total=150000, cantidad=5)
    boleta_creado = create_boleta(boleta, db)
    obtenter_boleta = get_boleta(boleta_creado.id,db)
    assert obtenter_boleta
    assert obtenter_boleta.id == 2

def test_update_boleta(db):
    boleta = schemas.boletas(id=3,orden_id=3, fecha_emision="23 de septiembre", monto_total=150000, cantidad=5)
    boleta_creado = create_boleta(boleta, db)
    nueva_boleta = schemas.boletaUpdate(orden_id=4,fecha_emision="24 de septiembre", monto_total=2200, cantidad=10)
    boleta_actualizada = update_boleta(boleta_creado.id, nueva_boleta, db)
    assert boleta_actualizada
    assert boleta_actualizada.id == boleta_creado.id
    assert boleta_actualizada.orden_id == nueva_boleta.orden_id
    assert boleta_actualizada.fecha_emision == nueva_boleta.fecha_emision
    assert boleta_actualizada.monto_total == nueva_boleta.monto_total
    assert boleta_actualizada.cantidad == nueva_boleta.cantidad
    
def test_get_boletas(db):
    obtener_boletas = get_boletas(db)   
    assert obtener_boletas
    assert obtener_boletas == db.query(models.Boletas_Facturas).all()
    
def test_delete_boleta(db):
    borrar_boleta = delete_boleta(2,db)
    assert borrar_boleta is None
    
    boleta_eliminada = db.query(models.Boletas_Facturas).filter(models.Boletas_Facturas.id == 2).first()
    assert boleta_eliminada is None    