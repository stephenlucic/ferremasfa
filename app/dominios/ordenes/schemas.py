from pydantic import BaseModel
from typing import Optional

class ordenes(BaseModel):
    id: Optional[int]=None
    fecha_orden: str
    usuario_id: int
    estado:str

class ordenesUpdate(BaseModel):
    fecha_orden: str
    usuario_id: int
    estado:str
        


