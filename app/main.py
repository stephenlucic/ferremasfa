from fastapi import FastAPI
from app.routers import usuarios,auth, ordenes
from .database import engine,Base
from fastapi.responses import RedirectResponse

app=FastAPI(
    title='Ferremas',
    description='Api que presta servicios a una ferretería',
    version='0.0.1'
)

Base.metadata.create_all(bind=engine)

@app.get('/' ,tags=["Principal"])
def Redirect():
    return RedirectResponse(url="/docs/")

app.include_router(auth.login_user)
app.include_router(usuarios.routerUsuario)
app.include_router(ordenes.routerOrdenes)