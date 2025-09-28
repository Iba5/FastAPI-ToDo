from pydantic import BaseModel
# from datetime import datetime
from typing import Optional

class tsk(BaseModel):
    id : int
    name: str
    create_time: str
    # end_time: str | None
    finished: bool

class UpdateTask(BaseModel):
    name:Optional[str]
    # end_time:Optional[str]
    finished:Optional [bool]

class CreateTask(BaseModel):
    name: str
   # end_time: str | None
    finished: bool=False
            

"""
--> THE CHALLENGES FACED WHILE CREATING THIS TASK CLASS:
    1. Finding a way for a user to add end date in such a way
    which won't conflict the format of the start date 
"""
"""
What I learn is:
After creating your model group them 
based on the intent, such that the 
create,update and respond are separate 
basemodels but with some similarities
only the purpose differs

->  Here I created the basic structure of how the data will be in the db with ref
    to my db.
->  So what happens here is when I create I will pass in the create task which is
    has the structure responsible for the operation and then the Id I wont pass because
    the DB is providing that for us
->  What happens is the actual base model is put to use when I now want to 
    retrieve data since it aligns to all the columns of the DB
"""