from repository.info import *
from models.task import Task
from fastapi import HTTPException

class services:
    def __init__(self,repo:Trepo):
        self.repo = repo
    
    def CreateToDo(self,inf:Task):
        return self.repo.AddTask(inf)
    
    def UpdateToDo(self, id:int,inf:Task):
        temp= self.repo.UpdateTask(id,inf)
        if not temp:
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return temp
    
    def DeleteTask(self,id:int):
        if not self.repo.DeleteTask(id):
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return {"message":"id:{id} delete successful"}
    def DisplayTodo(self,id:int):
        temp= self.repo.DisplayTask(id)
        if not temp:
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return temp
    
    def DisplayAll(self):
        return self.repo.DisplayAll()
    
    def DisplayFinished(self):
        return self.repo.FinishedTask()
    
