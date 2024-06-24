from pydantic import BaseModel
from typing import Optional

class oferta(BaseModel):
    id: Optional[int]=None
    descuento: float
    fecha_inicio: str
    fecha_fin:str
    sucursal_id: int
    producto_id: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'descuento':0.5,
                'fecha_inicio':"02/01/2024",
                'fecha_fin':"02/01/2024",
                'sucursal_id': 1,
                'producto_id': 1              
            }
        }
    } 

class ofertaUpdate(BaseModel):
    descuento: float
    fecha_inicio: str
    fecha_fin:str
    sucursal_id: int
    producto_id: int

    model_config = {
        'json_schema_extra':{
            'example':{
                'descuento':0.5,
                'fecha_inicio':"02/01/2024",
                'fecha_fin':"02/01/2024",
                'sucursal_id': 1,
                'producto_id': 1              
            }
        }
    }
        


