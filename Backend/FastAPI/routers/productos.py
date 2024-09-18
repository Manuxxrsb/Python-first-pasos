from fastapi import APIRouter

router = APIRouter(prefix="/productos",tags=["productos"]) 

"""el prefix es una guia para las rutas de abajo le indicamos en si lo que lleva la 
url ejemplo sin prefix -> localhost:puerto/productos/
url ejemplo con prefix -> localhost:puerto/productos/

la diferencia esta en la ruta del ruter que nos ahorra agregar el producto siempre antes del / 


"""
                                        

productos_list = [{"producto 1":"jabon"},
            {"producto 2":"lentes"},
            {"producto 3":"polera"}]

@router.get("/")
async def productos():
    return productos_list

@router.get("/{id:int}")
async def trae_usuario(id:int):
    return productos_list[id]