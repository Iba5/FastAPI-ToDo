from repository.info import *
from models.task import *
from models.Dto import *
from fastapi import HTTPException

class services:
    
    def __init__(self,repo:Trepo):
        self.repo = repo
    
    
    def CreateToDo(self,create:CreateTask):
        self.repo.AddTaskDB(create)
    
    
    def UpdateToDo(self, id:int, update:UpdateTask):
        temp= self.repo.UpdateTaskDB(id,update)
        if not temp:
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return temp
    
    
    def DeleteTask(self,id:int):
        if not self.repo.DeleteTaskDB(id):
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return 
    
    
    def DisplayTodo(self,id:int):
        temp= self.repo.DisplayTaskDB(id)
        if not temp:
            raise HTTPException(status_code=404, detail=f"Invalid Id, id:{id} Not Found")
        return temp
    
    
    def DisplayAll(self):
        return self.repo.DisplayAllDB()
    
    
    def DisplayFinished(self, id:int, update:UpdateTask):
        return self.repo.FinishedTasksDB(id,update)
    
    def DisplayAllDone(self):
        return self.repo.DisplayAllFinished()
