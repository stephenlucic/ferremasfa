import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.usuarios import models, schemas
from ..dominios.usuarios.repositorio import create_usuario,get_usuario,get_usuarios,update_usuario,delete_usuario

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

def test_create_usuario(db):
    usuario = schemas.usuario(id=1,nombre="Juanito", apellidos="Ayala", email="juanitoayala123@gmail.com", direccion="La bala 123")
    usuario_creado = create_usuario(usuario, db)
    assert usuario_creado.id == 1
    assert usuario_creado.nombre == "Juanito"
    assert usuario_creado.apellidos == "Ayala"
    assert usuario_creado.email == "juanitoayala123@gmail.com"
    assert usuario_creado.direccion == "La bala 123"

def test_get_usuario(db):
    usuario = schemas.usuario(id=2,nombre="Juanito", apellidos="Ayala", email="juanitoayala123@gmail.com", direccion="La bala 123")
    usuario_creado = create_usuario(usuario, db)
    obtener_usuario = get_usuario(usuario_creado.id,db)
    assert obtener_usuario
    assert obtener_usuario.id == 2
    
def test_update_usuario(db):
    usuario = schemas.usuario(id=3,nombre="pedrio", apellidos="martinez", email="martinez@gmail.com", direccion="ayahuasca 222")
    usuario_creado = create_usuario(usuario, db)
    nueva_usuario = schemas.usuarioUpdate(nombre="pedro", apellidos="carrasco", email="carrasco@gmail.com", direccion="flores 222")
    usuario_actualizada = update_usuario(usuario_creado.id, nueva_usuario, db)
    assert usuario_actualizada
    assert usuario_actualizada.id == usuario_creado.id
    assert usuario_actualizada.nombre == nueva_usuario.nombre
    assert usuario_actualizada.apellidos == nueva_usuario.apellidos
    assert usuario_actualizada.email == nueva_usuario.email
    assert usuario_actualizada.direccion == nueva_usuario.direccion
    
def test_get_usuarios(db):
    obtener_usuario = get_usuarios(db)   
    assert obtener_usuario
    assert obtener_usuario == db.query(models.Usuario).all()
    
def test_delete_usuario(db):
    borrar_usuario = delete_usuario(2,db)
    assert borrar_usuario is None  
    
    usuario_eliminada = db.query(models.Usuario).filter(models.Usuario.id == 2).first()
    assert usuario_eliminada is None      