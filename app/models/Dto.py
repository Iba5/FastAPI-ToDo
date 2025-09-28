from sqlmodel import SQLModel,Field
from datetime import datetime

class Task(SQLModel,table=True):
    id : int = Field(primary_key=True)
    name: str = Field(nullable=False)
    create_time: datetime =Field(default_factory=datetime.now)
#    end_time: Optional[datetime] | None=None
    finished: bool=Field(default=False)

"""
So in this is the table design which is 
being implemented to the DB
however there will be some conversions
such as an expected date of finishing will be inputed 
by the user so it will be in string format and
then be converted to datetime in the repository after it has 
been extracted
"""