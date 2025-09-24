from fastapi import APIRouter
from models.task import *
from repository.info import *

router = APIRouter()

@router.get("/todos/{id}")
def display(id:int):
    return


@router.get("/todos")
def DisplayAll():
    return


@router.post("/todos/add")
def CreateToDo():
    return


@router.put("/todos/update/{id}")
def UpdateTodo():
    return
    #raise HTTPException(status_code=404, detail="{Id} Not found")