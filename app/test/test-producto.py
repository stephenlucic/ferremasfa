import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.productos import models, schemas
from ..dominios.productos.repositorio import create_producto, get_producto, get_productos, delete_producto, update_producto
from ..dominios.productos.servicio import create_producto, get_producto, get_productos, update_producto, delete_producto

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

def test_create_producto(db):
    producto = schemas.productos(id=22, nombre="Taladro", descripcion="Taladro bauker", precio= 50000, categoria="maquinas")
    producto_creado = create_producto(producto, db)
    assert producto_creado.id == 22
    assert producto_creado.nombre == "Taladro"
    assert producto_creado.descripcion == "Taladro bauker"
    assert producto_creado.precio == 50000
    assert producto_creado.categoria == "maquinas"

def test_get_producto(db):
    producto = producto = schemas.productos(id=10, nombre="Taladro", descripcion="Taladro bauker", precio= 50000, categoria="maquinas")
    producto_creado = create_producto(producto, db)
    obtenter_producto = get_producto(producto_creado.id,db)
    assert obtenter_producto
    assert obtenter_producto.id == 10