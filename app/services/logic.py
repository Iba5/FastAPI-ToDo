from repository.info import *
from fastapi import HTTPException

class services:
    def __init__(self,repo:Trepo):
        self.repo = repo
    
    def CreateToDo(self):
        return self.repo.AddTask
    
    def UpdateToDo(self, id:int):
        if not id:
            raise HTTPException(status_code=404, detail="Invalid Id, id:{id} Not Found")
        temp= self.repo.UpdateTask(id)
        return 
    
    def DeleteTask(self,id:int):
        if not self.repo.DeleteTask(id):
            raise HTTPException(status_code=404, detail="Invalid Id, id:{id} Not Found")
        return {"message":"id:{id} delete successful"}
    def DisplayTodo(self,id:int):
        temp= self.repo.DisplayTask(id)
        if not temp:
            raise HTTPException(status_code=404, detail="Invalid Id, id:{id} Not Found")
        return temp
    
    def DisplayAll(self):
        return self.repo.DisplayAll()
    
    def DisplayFinished(self):
        return self.repo.FinishedTask()
    
