from pydantic import BaseModel
from typing import Optional

class usuario(BaseModel):
    id: Optional[int]=None
    nombre: str
    apellidos:str
    email: str
    direccion:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'nombre':"juanito",
                'apellidos':"perez perez",
                'email':"juanito@example.com",
                'direccion':"calle 123, en algún lugar"
            }
        }
    }

class usuarioUpdate(BaseModel):
    nombre: str
    apellidos:str
    email: str
    direccion:str 

    model_config = {
        'json_schema_extra':{
            'example':{
                'nombre':"juanito",
                'apellidos':"perez perez",
                'email':"juanito@example.com",
                'direccion':"calle 123, en algún lugar"
            }
        }
    }

class user(BaseModel):
    email:str
    password:str   
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'email':"yerko@gmail.com",
                'password':"123"
            }
        }
    }
