from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter(prefix="/user",tags=["user"])

#inicia el seridor con: uvicorn users:app --reload

#entidad - objeto user

class User(BaseModel):
    id: int
    name: str
    lasname: str
    age: int

fakedb = [User(id=1,name="Manuel",lasname="Solis",age=23),User(id=2,name="Matias",lasname="Solis",age=13),User(id=3,name="Miguel",lasname="Solis",age=43)]


@router.get("/JSON")
async def users():
    return [{"mensaje":"API de usuarios"},
            {"mensaje":"API de personas"},
            {"mensaje":"que pasaaaa"}]

@router.get("/class")
async def users2():
    return User(id=0 ,name="Manuel",lasname="solis",age=23)

@router.get("/BD")
async def usuarios_bd():
    return fakedb

@router.get("/busca/{id}")
async def buscar(id:int):
    indice = fakedb.User.id().index(id)
    return indice

@router.post("/usuario/")
async def crea_usuario(usuario:User):
    fakedb.append(usuario)

