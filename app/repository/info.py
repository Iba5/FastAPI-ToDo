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
    
    def UpdateTask(self, id:int, inf:Task)->Tasks:
        for index, i in enumerate(self.data):
            if  i.id == id:
                temp = Tasks(id=index, **inf.model_dump())
                self.data[index]=temp
                return temp
        raise     
        
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
    """