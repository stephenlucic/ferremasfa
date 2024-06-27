import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.reportes import models, schemas
from ..dominios.reportes.repositorio import create_reporte,get_reporte,get_reportes,update_reporte,delete_reporte


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

def test_create_reporte(db):
    reporte = schemas.reportes(id=1,usuario_id=1, tipo="venta", fecha_generada="12 de marzo")
    reporte_creado = create_reporte(reporte, db)
    assert reporte_creado.id == 1
    assert reporte_creado.usuario_id == 1
    assert reporte_creado.tipo == "venta"
    assert reporte_creado.fecha_generada == "12 de marzo"

def test_get_reporte(db):
    reporte = schemas.reportes(id=2,usuario_id=2, tipo="venta", fecha_generada="12 de marzo")
    reporte_creado = create_reporte(reporte, db)
    obtenter_reporte = get_reporte(reporte_creado.id,db)
    assert obtenter_reporte
    assert obtenter_reporte.id == 2
    
def test_update_reporte(db):
    reporte = schemas.reportes(id=3,usuario_id=4, tipo="cotizaciones", fecha_generada="16 de marzo")
    reporte_creado = create_reporte(reporte, db)
    nueva_reporte = schemas.reportesUpdate(usuario_id=3, tipo="balance del año", fecha_generada="25 de marzo")
    reporte_actualizada = update_reporte(reporte_creado.id, nueva_reporte, db)
    assert reporte_actualizada
    assert reporte_actualizada.id == reporte_creado.id
    assert reporte_actualizada.usuario_id == nueva_reporte.usuario_id
    assert reporte_actualizada.tipo == nueva_reporte.tipo
    assert reporte_actualizada.fecha_generada == nueva_reporte.fecha_generada
    
    
def test_get_reportes(db):
    obtener_reporte = get_reportes(db)   
    assert obtener_reporte
    assert obtener_reporte == db.query(models.Reportes).all()
    
def test_delete_reporte(db):
    borrar_reporte = delete_reporte(2,db)
    assert borrar_reporte is None  
    
    reporte_eliminada = db.query(models.Reportes).filter(models.Reportes.id == 2).first()
    assert reporte_eliminada is None 