from pydantic import BaseModel
from typing import Optional

class sucursales(BaseModel):
    id: Optional[int]=None
    nombre: str
    direccion: str

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'nombre':"bellavista...",
                'direccion':"calle 123, comuna, ciudad"             
            }
        }
    } 

class sucursalUpdate(BaseModel):
    nombre: str
    direccion: str

    model_config = {
        'json_schema_extra':{
            'example':{
                'nombre':"bellavista...",
                'direccion':"calle 123, comuna, ciudad"              
            }
        }
    }
        


