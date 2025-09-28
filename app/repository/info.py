from typing import List
from fastapi import Depends
from abc import ABC,abstractmethod
from sqlmodel import Session, select
from models.task import *
from models.Dto import *
from db.sessions import get_db

class InterfaceRepo(ABC):
    @abstractmethod
    def AddTaskDB(self,CreateT:CreateTask)->Task:
        pass
    @abstractmethod
    def UpdateTaskDB(self,id:int, UpdateT:UpdateTask)->Optional[Task]:
        pass
    @abstractmethod
    def DeleteTaskDB(self,id:int)->Optional[Task]:
        pass
    @abstractmethod
    def DisplayTaskDB(self,id:int)->Optional[Task]:
        pass
    @abstractmethod
    def DisplayAllDB(self)->Task:
        pass
    @abstractmethod
    def FinishedTasksDB(self ,id:int ,UpdateT:UpdateTask)->Optional[Task]:
        pass
    @abstractmethod
    def get_by_id(self,id:int)->Optional[Task]:
        pass


class Trepo(InterfaceRepo):
    def __int__(self,db:Session=Depends(get_db)):
        self.db=db

    def get_by_id(self,id:int):
        return self.db.exec(select(Task).where(Task.id==id)).first()
    
    def AddTaskDB(self,CreateT:CreateTask):
        temp = Task(**CreateT.model_dump())
        self.db.add(temp)
        self.db.commit()
        self.db.refresh(temp)
        return temp
    
    def UpdateTaskDB(self,id:int, UpdateT:UpdateTask):
        temp = Task(**UpdateT.model_dump())
        task = self.get_by_id(id)
        if task:
            task=temp
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        return task
    
    def DeleteTaskDB(self,id:int):
        task = self.get_by_id(id)
        if task:
            self.db.delete(task)
            self.db.commit()
        return task
    
    def DisplayTaskDB(self,id:int):
        result =self.db.exec(select(Task).where(Task.id==id))
        task =  result.first()
        return task
    
    def DisplayAllDB(self)->Task:
        return self.db.exec(select(Task)).all()
     
    def FinishedTasksDB(self ,id:int ,UpdateT:UpdateTask):
        task = self.get_by_id(id)
        if task:
            for key, value in UpdateT.model_dump().items():
                setattr(task, key, value)
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        return task
    
    def DisplayAllFinished(self):
        return self.db.exec(select(Task).where(Task.finished==True)).all()
        


"""
    What I learnt today using this inbuilt:
    How the functions behave
    how to use the List comprehensions
    how an interface is created in python
    
if using model_dump() since we are using pydantic v2:

1. you look at the class Task which is the base model
2. Connect it to the class Tasks which contains the id
3. You create a Lists of the structure class Task
4. Since the Id is to be generated automatically you then set it to a specific val

How to add the data:

1. When you add, always take a Task, assign an id, and convert to Tasks.
2. model_dump() is just a way of unpacking the Task fields into Tasks.
3. After you create a Tasks object, push it into data

How to update data:

1. The update function must receive:
2. The id (to find the right task).
3. The new Task data (to replace/update).
4. Then you must:
5. Loop over data.
6. Find the task with matching id.
7. Replace it inside the list (data[index] = new_object)

How to see things in this repo:

    Treat Task as the DTO for input validation. Inside my repository, 
    I only persist Tasks, which includes the business identifier (id). 
    That lets me query, update, and manage tasks reliably. 
    The list is effectively my fake database table, 
    so it must contain entities (Tasks) not DTOs (Task).

    
Updated : 28/09/25
I have managed to connect the db as well as sessions, However the
challenge is now in converting user input end time to be datetime or vice versa
"""