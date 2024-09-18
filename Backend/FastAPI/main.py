from fastapi import FastAPI
from routers import productos , users
from fastapi.staticfiles import StaticFiles


app = FastAPI()

#url local: http://127.0.0.1:8000

#routers   //para conexion entre apis
app.include_router(productos.router)     #con cada router genero la conexion a la api como un microservicio en el mismo
app.include_router(users.router)  #router que une la API general conla API Usuarios

#documentos staticos
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():  #el uso de la palabra async le dice al servidor que puede ejecutar otras cosas mientras
    return "! hola FastAPI !"   #por ejemplo si la request es grande el server puede carga mientras la vista de la pagina 

#url local: http://127.0.0.1:8000/

@app.get("/url")
async def devuelve_url():
    return { "Url": "https://www.google.cl"}    #retorno esta en formato JSON por eso entre llaves

#url local: http://127.0.0.1:8000/url


#inicia el servidor: uvicorn main:app --reload
#detener el servidor: ctrl + c 

