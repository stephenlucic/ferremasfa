from pydantic import BaseModel
from typing import Optional

class productos(BaseModel):
    id: Optional[int]=None
    nombre: str
    descripcion: str
    precio:float
    categoria:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'nombre':"martillo",
                'descripcion':"este martillo es de acero....",
                'precio': 15000,
                'categoria':"herramientas"              
            }
        }
    }

class productoUpdate(BaseModel):
    nombre: str
    descripcion: int
    precio:float
    categoria:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'nombre':"martillo",
                'descripcion':"este martillo es de acero....",
                'precio': 15000,
                'categoria':"herramientas"              
            }
        }
    }

        