from pydantic import BaseModel
from typing import Optional

class usuario(BaseModel):
    id: Optional[int]=None
    nombre: str
    email: str
    
