from pydantic import BaseModel
from typing import Optional

class usuario(BaseModel):
    id: Optional[int]=None
    nombre: str
    apellidos:str
    email: str
    direccion:str

class usuarioUpdate(BaseModel):
    nombre: str
    apellidos:str
    email: str
    direccion:str 

class user(BaseModel):
    email:str
    password:str   
    
