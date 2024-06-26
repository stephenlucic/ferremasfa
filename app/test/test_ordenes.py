import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.ordenes import models, schemas
from ..dominios.ordenes.repositorio import create_orden,get_orden,get_ordenes,update_orden,delete_orden

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
    obtenter_orden = get_orden(orden_creada.id,db)
    assert obtenter_orden
    assert obtenter_orden.id == 2
    
def test_update_orden(db):
    ordenes = schemas.ordenes(id=3,fecha_orden="1 de junio", usuario_id=4, estado="activo")
    ordenes_creado = create_orden(ordenes, db)
    nueva_ordenes = schemas.ordenesUpdate(fecha_orden="10 de junio", usuario_id=3, estado="pendiente")
    ordenes_actualizada = update_orden(ordenes_creado.id, nueva_ordenes, db)
    assert ordenes_actualizada
    assert ordenes_actualizada.id == ordenes_creado.id
    assert ordenes_actualizada.fecha_orden == nueva_ordenes.fecha_orden
    assert ordenes_actualizada.usuario_id == nueva_ordenes.usuario_id
    assert ordenes_actualizada.estado == nueva_ordenes.estado
    
def test_get_ordenes(db):
    obtener_ordenes = get_ordenes(db)   
    assert obtener_ordenes
    assert obtener_ordenes == db.query(models.Ordenes).all()
    
def test_delete_orden(db):
    borrar_orden = delete_orden(2,db)
    assert borrar_orden is None
    
    orden_eliminada = db.query(models.Ordenes).filter(models.Ordenes.id == 2).first()
    assert orden_eliminada is None
    
    
    