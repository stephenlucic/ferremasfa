import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..dominios.usuarios import models, schemas
from ..dominios.usuarios.repositorio import create_usuario,get_usuario,get_usuarios,update_usuario,delete_usuario
from ..dominios.usuarios.servicio import create_usuario,get_usuario,get_usuarios,update_usuario,delete_usuario

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