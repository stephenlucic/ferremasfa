from pydantic import BaseModel
from typing import Optional

class reportes(BaseModel):
    id: Optional[int]=None
    usuario_id: int
    tipo:str
    fecha_generada:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'usuario_id':1,
                'tipo':"ventas totales",
                'fecha_generada':"30/12/2024"              
            }
        }
    }

class reportesUpdate(BaseModel):
    usuario_id: int
    tipo:str
    fecha_generada:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'usuario_id':1,
                'tipo':"ventas totales",
                'fecha_generada':"30/12/2024"              
            }
        }
    }
        

