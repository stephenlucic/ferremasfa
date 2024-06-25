import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.inventarios import models, schemas
from ..dominios.inventarios.repositorio import create_inventario,get_inventario,get_inventarios,update_inventario,delete_inventario
from ..dominios.inventarios.servicio import create_inventario,get_inventario,get_inventarios,update_inventario,delete_inventario

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

def test_create_inventario(db):
    inventario = schemas.inventarios(id=1,cantidad=50,sucursal_id=1,producto_id=1)
    inventario_creado = create_inventario(inventario, db)
    assert inventario_creado.id == 1
    assert inventario_creado.cantidad == 50
    assert inventario_creado.sucursal_id == 1
    assert inventario_creado.producto_id == 1


def test_get_inventario(db):
    inventario = inventario = schemas.inventarios(id=2,cantidad=100,sucursal_id=2, producto_id=2)
    inventario_creado = create_inventario(inventario, db)
    obtenter_inventario = get_inventario(inventario_creado.id,db)
    assert obtenter_inventario
    assert obtenter_inventario.id == 2