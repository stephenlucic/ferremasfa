import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ofertas import models, schemas
from ..dominios.ofertas.repositorio import create_oferta,get_oferta,get_ofertas,update_oferta,delete_oferta
from ..dominios.ofertas.servicio import create_oferta,get_oferta,get_ofertas,update_oferta,delete_oferta
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

def test_create_oferta(db):
    oferta = schemas.oferta(id=1,descuento=5000,fecha_inicio="13 de mayo",fecha_fin="25 de junio", sucursal_id=1, producto_id=1)
    oferta_creada = create_oferta(oferta, db)
    assert oferta_creada.id == 1
    assert oferta_creada.descuento == 5000
    assert oferta_creada.fecha_inicio == "13 de mayo"
    assert oferta_creada.fecha_fin == "25 de junio"
    assert oferta_creada.sucursal_id == 1
    assert oferta_creada.producto_id == 1

def test_get_producto(db):
    oferta = schemas.oferta(id=2,descuento=5000,fecha_inicio="13 de mayo",fecha_fin="25 de junio", sucursal_id=2, producto_id=2)
    oferta_creada = create_oferta(oferta, db)
    obtenter_producto = get_oferta(oferta_creada.id,db)
    assert obtenter_producto
    assert obtenter_producto.id == 2