import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.reportes import models, schemas
from ..dominios.reportes.repositorio import create_reporte,get_reporte,get_reportes,update_reporte,delete_reporte
from ..dominios.reportes.servicio import create_reporte,get_reporte,get_reportes,update_reporte,delete_reporte

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