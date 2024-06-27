import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ofertas import models, schemas
from ..dominios.ofertas.repositorio import create_oferta,get_oferta,get_ofertas,update_oferta,delete_oferta

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

def test_get_oferta(db):
    oferta = schemas.oferta(id=2,descuento=5000,fecha_inicio="13 de mayo",fecha_fin="25 de junio", sucursal_id=2, producto_id=2)
    oferta_creada = create_oferta(oferta, db)
    obtenter_producto = get_oferta(oferta_creada.id,db)
    assert obtenter_producto
    assert obtenter_producto.id == 2
    
def test_update_oferta(db):
    oferta = oferta = schemas.oferta(id=4,descuento=6000,fecha_inicio="14 de mayo",fecha_fin="25 de dic", sucursal_id=4, producto_id=4)
    oferta_creado = create_oferta(oferta, db)
    nuevo_oferta = schemas.ofertaUpdate(descuento=400,fecha_inicio="16 de mayo",fecha_fin="29 de dic", sucursal_id=3, producto_id=3)
    oferta_actualizado = update_oferta(oferta_creado.id, nuevo_oferta, db)
    assert oferta_actualizado
    assert oferta_actualizado.id == oferta_creado.id
    assert oferta_actualizado.descuento == nuevo_oferta.descuento
    assert oferta_actualizado.fecha_fin == nuevo_oferta.fecha_fin
    assert oferta_actualizado.sucursal_id == nuevo_oferta.sucursal_id
    assert oferta_actualizado.producto_id == nuevo_oferta.producto_id    