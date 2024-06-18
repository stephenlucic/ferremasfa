from pydantic import BaseModel
from typing import Optional

class ordenes(BaseModel):
    id: Optional[int]=None
    detalle: str
    usuario_id: int
    producto_id:int
