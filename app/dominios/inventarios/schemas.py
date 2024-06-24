from pydantic import BaseModel
from typing import Optional

class inventarios(BaseModel):
    id: Optional[int]=None
    cantidad: int
    sucursal_id: int
    producto_id:int

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'cantidad':1,
                'sucursal_id':1,
                'producto_id':1            
            }
        }
    } 

class inventarioUpdate(BaseModel):
    cantidad: int
    sucursal_id: int
    producto_id:int

    model_config = {
        'json_schema_extra':{
            'example':{
                'cantidad':1,
                'sucursal_id':1,
                'producto_id':1             
            }
        }
    }
        


