import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.sucursales import models, schemas
from ..dominios.sucursales.repositorio import create_sucursal,get_sucursal,get_sucursales,update_sucursal,delete_sucursal


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
    
def test_update_sucursal(db):
    sucursal = schemas.sucursales(id=3,nombre="Santiago centro", direccion="Baquedano 123")
    sucursal_creado = create_sucursal(sucursal, db)
    nueva_sucursal = schemas.sucursalUpdate(nombre="rancagua", direccion="no existe")
    sucursal_actualizada = update_sucursal(sucursal_creado.id, nueva_sucursal, db)
    assert sucursal_actualizada
    assert sucursal_actualizada.id == sucursal_creado.id
    assert sucursal_actualizada.nombre == nueva_sucursal.nombre
    assert sucursal_actualizada.direccion == nueva_sucursal.direccion
   
   
def test_get_sucursales(db):
    obtener_sucursal = get_sucursales(db)   
    assert obtener_sucursal
    assert obtener_sucursal == db.query(models.Sucursales).all()
    
def test_delete_sucursal(db):
    borrar_sucursal = delete_sucursal(2,db)
    assert borrar_sucursal is None  
    
    sucursal_eliminada = db.query(models.Sucursales).filter(models.Sucursales.id == 2).first()
    assert sucursal_eliminada is None    