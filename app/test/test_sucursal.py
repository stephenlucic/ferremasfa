import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.sucursales import models, schemas
from ..dominios.sucursales.repositorio import create_sucursal,get_sucursal,get_sucursales,update_sucursal,delete_sucursal
from ..dominios.sucursales.servicio import create_sucursal,get_sucursal,get_sucursales,update_sucursal,delete_sucursal

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

def test_create_sucursal(db):
    sucursal = schemas.sucursales(id=1,nombre="Santiago centro", direccion="Baquedano 123")
    sucursal_creada = create_sucursal(sucursal, db)
    assert sucursal_creada.id == 1
    assert sucursal_creada.nombre == "Santiago centro"
    assert sucursal_creada.direccion == "Baquedano 123"


def test_get_sucursal(db):
    sucursal = schemas.sucursales(id=2,nombre="Santiago centro", direccion="Baquedano 123")
    sucursal_creada = create_sucursal(sucursal,db)
    obtenter_sucursal = get_sucursal(sucursal_creada.id, db)
    assert obtenter_sucursal
    assert obtenter_sucursal.id == 2