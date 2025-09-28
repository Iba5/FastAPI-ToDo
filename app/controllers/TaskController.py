from fastapi import APIRouter
from models.task import *
from services.logic import *
from db.connections import *

router = APIRouter()
repo=Trepo()
serv = services(repo)

@router.get("/todos/{id}")
async def Display(id:int):
    return serv.DisplayTodo(id)


@router.get("/todos",status_code=200)
async def DisplayAll():
    return serv.DisplayAll()

@router.get("/todos/finished/")
async def DisplayFinishedOne():
    return serv.DisplayAllDone()

@router.post("/todos/add",status_code=201)
def createToDo(create:CreateTask):
    return  serv.CreateToDo(create)


@router.patch("/todos/update/{id}")
def UpdateTodo(id:int,update:UpdateTask):
    serv.UpdateToDo(id,update)
