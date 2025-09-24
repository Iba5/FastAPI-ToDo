from pydantic import BaseModel

class Task(BaseModel): 
    task: str
    done : bool= False

class Tasks(Task):
    id:int

"""
--> THE CHALLENGES FACED WHILE CREATING THIS TASK CLASS:
    1. Finding a way for a user to add end date in such a way
    which won't conflict the format of the start date 
"""