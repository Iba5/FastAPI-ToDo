from abc import ABC,abstractmethod
from models.task import *
from typing import List

class InterfaceRepo(ABC):
    @abstractmethod
    def AddTask(self,inf:Task)->Tasks:
        pass
    @abstractmethod
    def UpdateTask(self, id:int, inf:Task)->Tasks:
        pass
    @abstractmethod
    def DeleteTask(self,id:int):
        pass
    @abstractmethod
    def DisplayTask(self, id:int):
        pass
    @abstractmethod
    def DisplayAll(self):
        pass
    @abstractmethod
    def FinishedTasks(self, id:int):
        pass


class Trepo:
    def __init__(self):
        self.data:List[Tasks]=[]
        self.id_counter=1
    
    def AddTask(self,inf:Task)->Tasks:
        temp=Tasks(id=self.id_counter,**inf.model_dump())
        self.data.append(temp)
        self.id_counter+=1
        return temp
    
    def UpdateTask(self, id:int, inf:Task):
        for index, i in enumerate(self.data):
            if  i.id == id:
                temp = Tasks(id=i.id, **inf.model_dump())
                self.data[index]=temp
                return temp
        return 
        
    def DeleteTask(self, id:int):
        for index ,i in enumerate(self.data):
            if i.id == id:
                self.data.pop(index)
                return True
        return False        

    def DisplayTask(self, id: int):
        temp=[i for i in self.data if i.id==id]
        return temp

    def DisplayAll(self):
        return self.data
    
    def FinishedTask(self):
        finished=[i for i in self.data if i.done is True]
        return finished
    



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
3. After you create a Tasks object, push it into self.data

How to update data:

1. The update function must receive:
2. The id (to find the right task).
3. The new Task data (to replace/update).
4. Then you must:
5. Loop over self.data.
6. Find the task with matching id.
7. Replace it inside the list (self.data[index] = new_object)

How to see things in this repo:

    Treat Task as the DTO for input validation. Inside my repository, 
    I only persist Tasks, which includes the business identifier (id). 
    That lets me query, update, and manage tasks reliably. 
    The list is effectively my fake database table, 
    so it must contain entities (Tasks) not DTOs (Task).
"""