from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from ..user_jwt import validateToken




class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data= validateToken(auth.credentials)
        if data['email']!= 'yerko@gmail.com':
            raise HTTPException(status_code=403, detail="'Credenciales incorrectas'")
        




