import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.inventarios import models, schemas
from ..dominios.inventarios.repositorio import create_inventario,get_inventario,get_inventarios,update_inventario,delete_inventario


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

def test_create_inventario(db):
    inventario = schemas.inventarios(id=1,cantidad=50,sucursal_id=3, producto_id=4)
    inventario_creado = create_inventario(inventario, db)
    print(inventario_creado.id)
    assert inventario_creado.id ==1
    assert inventario_creado.cantidad == 50
    assert inventario_creado.sucursal_id == 3
    assert inventario_creado.producto_id == 4


def test_get_inventario(db):
    inventario = inventario = schemas.inventarios(id=2,cantidad=100,sucursal_id=2, producto_id=2)
    inventario_creado = create_inventario(inventario, db)
    obtenter_inventario = get_inventario(inventario_creado.id,db)
    assert obtenter_inventario
    assert obtenter_inventario.id == 2
    
def test_update_inventario(db):
    inventario = inventario = schemas.inventarios(id=6,cantidad=1006,sucursal_id=26, producto_id=26)
    inventario_creado = create_inventario(inventario, db)
    nuevo_inventario = schemas.inventarioUpdate(cantidad=1100,sucursal_id=8, producto_id=8)
    inventario_actualizado = update_inventario(inventario_creado.id, nuevo_inventario, db)
    assert inventario_actualizado
    assert inventario_actualizado.id == inventario_creado.id
    assert inventario_actualizado.cantidad == nuevo_inventario.cantidad
    assert inventario_actualizado.sucursal_id == nuevo_inventario.sucursal_id
    assert inventario_actualizado.producto_id == nuevo_inventario.producto_id
    
def test_get_inventarios(db):
    obtener_inventario = get_inventarios(db)   
    assert obtener_inventario
    assert obtener_inventario == db.query(models.Inventarios).all()
    
def test_delete_inventario(db):
    borrar_inventario = delete_inventario(2,db)
    assert borrar_inventario is None
    
    inventario_eliminada = db.query(models.Inventarios).filter(models.Inventarios.id == 2).first()
    assert inventario_eliminada is None
 