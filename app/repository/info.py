from models.task import Task,Tasks
from typing import List

class TaskRepo:
    def __init__(self):
        self.data:List[Task]=[]
        self.id_counter=1

    def AddTask(self,inf:Task)->Tasks:
        temp=Tasks(id=self.id_counter,**inf.model_dump())
        self.data.append(temp)
        self.id_counter+=1
        return temp
    
    def UpdateTask(self,id: int):
        for index, i in enumerate(self.data):
            if  index == id:
                temp = Tasks(id=index, **inf.model_dump())
                i = temp

                
