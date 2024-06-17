from fastapi import FastAPI
from app.routers import usuarios
from .database import engine,Base
from fastapi.responses import RedirectResponse

app=FastAPI(
    title='Ferremas',
    description='Api que presta servicios a una ferretería',
    version='0.0.1'
)

Base.metadata.create_all(bind=engine)

@app.get('/' ,tags=["Principal"])
def main():
    return RedirectResponse(url="/docs/")

app.include_router(usuarios.routerUsuario)