from fastapi import FastAPI , HTTPException , Depends
from pydantic import BaseModel
from typing import List , Annotated
import models

#importamos la base de datos
from database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine) #linea que exporta todas las tablas y columnas a postgress

#estas clases las usaremos para la validacion de datos , ponerlo en carpeta esquemas
class Item(BaseModel):
    id:int
    item_nombre:str

class Persona(BaseModel):
    id:int
    nombre:str
    cosas:List[Item]



#funcion que inicia la conexion con la bd usa funciones de database.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #al finalizar termina la conexion

db_dependency = Annotated[Session,Depends(get_db) ] ##creamos un conector auxiliar que abre y cierra la conexion a la bd en las funciones que sea utilizada para no dejar abierta la conexion


@app.get("/")
async def saluda():
    return {"mensaje": "Hola mundo"}

@app.post("/set_persona")
async def ingresa_persona(persona: Persona , db : db_dependency):
    persona_auxiliar = models.Persona(id=1,nombre="manuel") #se declara la conexion tipo orm por decirlo
    db.add(persona_auxiliar)
    db.commit()
    db.refresh(persona_auxiliar) #como para update creo
    item_auxiliar = models.Item(id=1,item_nombre="Reloj",dueno_id = persona_auxiliar.id)
    db.add(item_auxiliar)
    db.commit()


#------------------METODO C CREATE
@app.post("/Cpersona/{Persona}") #create para una persona con dependencia de otras tablas
async def crea_persona(persona: Persona,db:db_dependency):
    persona_auxiliar= models.Persona(id=persona.id,nombre=persona.nombre)   #creamos a la persona auxiliar para la funcion
    db.add(persona_auxiliar) #se agrega a la persona
    db.commit() #commit a la bd
    db.refresh(persona_auxiliar) #actualizamos la persona para evitar errores
    for item in persona.cosas:  #ciclo para agregar todos los objetos item es el tablename del model
        db_cosas = models.Item(id=item.id,item_nombre=item.item_nombre,dueno_id=persona_auxiliar.id) #creamos la lista de cosas de la persona
        db.add(db_cosas) #se agrega a la bd
    db.commit() #commit a la bd con los cambios


#------------------ METODO R READ
@app.get("/Rpersona/{nombre_persona}")
async def busca_persona(nombre_persona:str,db:db_dependency):
    resultado = db.query(models.Persona).filter(models.Persona.nombre == nombre_persona).first()   #si quitas el first trae a todos
    if not resultado:
        raise HTTPException(status_code=404,detail="No se encontro a la persona")
    return resultado

@app.get("/Ritem/{Item_nombre}")
async def busca_item(Item_nombre: str,db:db_dependency):
    resultado = db.query(models.Item).filter(models.Item.item_nombre == Item_nombre).first()
    if not resultado:
        raise HTTPException(status_code=404,detail="No se encontro el objeto")
    return resultado

#------------- METODO D DELETE 
@app.delete("/Ditem/{item_id}")
async def elimina_item(item_id:int , db:db_dependency):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()

    if not item:
        raise HTTPException(status_code=404,detail="No se encontro el objeto")
    
    #eliminamos el objeto
    db.delete(item)     #elimina la tabla item que contiene reloj
    db.commit()
    return {"detalle:":"Item eliminado exitosamente","item:":item}


#---------------- METODO U UPDATE
@app.put("/Ritem/{item_nombre}")
async def actualiza_item(item_nombre: str,nuevo:Item,db:db_dependency):
    #buscamos el item
    item = db.query(models.Item).filter(models.Item.item_nombre == item_nombre).first()

    #comprobamos
    if not item:
        raise HTTPException(status_code=404,detail="No se encuentra el item para actualizar")
    
    item.item_nombre = nuevo.item_nombre
    item.id = nuevo.id
    #pueden actualizarce varios campos de esa forma segun pasemos un nuevo objeto en JSON body
    db.commit()
    return {"detalle": "Ítem actualizado exitosamente", "item": item}

