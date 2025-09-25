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
    def DeleteTask(self,id:int)->Tasks:
        pass
    @abstractmethod
    def DisplayTask(self, id:int)->Tasks:
        pass
    @abstractmethod
    def DisplayAll(self):
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
        