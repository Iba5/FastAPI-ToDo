from fastapi import APIRouter
from models.task import *
from services.logic import *

router = APIRouter()
repo=Trepo()
serv = services(repo)

@router.get("/todos/{id}")
async def Display(id:int):
    return serv.DisplayTodo(id)


@router.get("/todos")
async def DisplayAll():
    return serv.DisplayAll()


@router.post("/todos/add")
def createToDo(inf:Task):
    return  serv.CreateToDo(inf)


@router.patch("/todos/update/{id}")
def UpdateTodo(id:int,inf:Task):
    temp = serv.UpdateToDo(id,inf)
    return temp


    