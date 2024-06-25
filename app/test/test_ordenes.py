import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ordenes import models, schemas
from ..dominios.ordenes.repositorio import create_orden,get_orden,get_ordenes,update_orden,delete_orden
from ..dominios.ordenes.servicio import create_orden,get_orden,get_ordenes,update_orden,delete_orden

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

def test_create_orden(db):
    ordenes = schemas.ordenes(id=1,fecha_orden="31 de junio", usuario_id=1, estado="activo")
    orden_creada = create_orden(ordenes, db)
    assert orden_creada.id == 1
    assert orden_creada.fecha_orden == "31 de junio"
    assert orden_creada.usuario_id == 1
    assert orden_creada.estado == "activo"


def test_get_orden(db):
    ordenes = schemas.ordenes(id=2,fecha_orden="31 de junio", usuario_id=2, estado="activo")
    orden_creada = create_orden(ordenes, db)
    obtenter_producto = get_orden(orden_creada.id,db)
    assert obtenter_producto
    assert obtenter_producto.id == 2