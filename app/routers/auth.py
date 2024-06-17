from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..dominios.usuarios import schemas
from ..user_jwt import createToken
from ..middleware.bearer_jwt import BearerJWT

login_user= APIRouter()
seguridad=BearerJWT()

@login_user.post('/login',tags=['authentificación'])
def login(user:schemas.user):
    if user.email == 'yerko@gmail.com' and user.password == '123':
        token:str=createToken(user.model_dump())
        print(token)
        return JSONResponse(content=token)
    