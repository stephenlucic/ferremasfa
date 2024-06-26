from pydantic import BaseModel
from typing import Optional

class ordenes(BaseModel):
    id: Optional[int]=None
    fecha_orden: str
    usuario_id: int
    estado:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'fecha_orden':"30/12/2024",
                'usuario_id':1,
                'estado':"terminado"              
            }
        }
    } 

class ordenesUpdate(BaseModel):
    fecha_orden: str
    usuario_id: int
    estado:str

    model_config = {
        'json_schema_extra':{
            'example':{
                'fecha_orden':"30/12/2024",
                'usuario_id':1,
                'estado':"terminado"              
            }
        }
    }
        


