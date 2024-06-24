from pydantic import BaseModel
from typing import Optional

class ventas(BaseModel):
    id: Optional[int]=None
    fecha_emision: str
    cantidad: int
    monto: float
    producto_id: int
    orden_id: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'fecha_emision':"30/12/2024",
                'cantidad': 1,
                'monto':10,
                'producto_id':1,
                'orden_id': 1           
            }
        }
    } 

class ventasUpdate(BaseModel):
    fecha_emision: str
    cantidad: int
    monto: float
    producto_id: int
    orden_id: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'fecha_emision':"30/12/2024",
                'cantidad': 1,
                'monto':10,
                'producto_id':1,
                'orden_id': 1            
            }
        }
    }
        


