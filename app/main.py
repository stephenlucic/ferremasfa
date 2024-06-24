from fastapi import FastAPI
from app.routers import usuarios, auth, ordenes, boleta, oferta, venta
from app.routers import productos, reportes, inventario, sucursal
from .database import engine,Base
from fastapi.responses import RedirectResponse

app=FastAPI(
    title='Ferremas',
    description='Api que presta servicios a una ferretería',
    version='0.8'
)

Base.metadata.create_all(bind=engine)

@app.get('/' ,tags=["Principal"])
def Redirect():
    return RedirectResponse(url="/docs/")

app.include_router(auth.login_user)
app.include_router(usuarios.routerUsuario)
app.include_router(ordenes.routerOrdenes)
app.include_router(productos.routerProducto)
app.include_router(reportes.routerReporte)
app.include_router(inventario.routerInventario)
app.include_router(sucursal.routerSucursales)
app.include_router(boleta.routerBoletas)
app.include_router(oferta.routerOfertas)
app.include_router(venta.routerVentas)