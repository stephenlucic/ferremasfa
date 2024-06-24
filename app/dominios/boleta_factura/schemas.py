from pydantic import BaseModel
from typing import Optional

class boletas(BaseModel):
    id: Optional[int]=None
    orden_id: int
    fecha_emision: str
    monto_total: float
    cantidad: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'orden_id':1,
                'fecha_emision':"30/12/2024",
                'monto_total':100,
                'cantidad': 10                 
            }
        }
    } 

class boletaUpdate(BaseModel):
    orden_id: int
    fecha_emision: str
    monto_total: float
    cantidad: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'orden_id':1,
                'fecha_emision':"30/12/2024",
                'monto_total':100,
                'cantidad': 10              
            }
        }
    }
        
