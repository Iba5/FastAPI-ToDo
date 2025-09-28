from sqlmodel import Session
from .connections import engine
from db.connections import *
from models.Dto import *

def create_db():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session

"""
SessionMaker:
->  This is the icing to the cake, It is the one which finalises
    the db to app connection as it is the one responsible for 
    communicating or converting from py to sql
     
->  When we set autocommit to false we are basically trying to
    make sure that the changes made to the DB will be commited
    by us

->  autoflash is also set to false so as to ensure that all the synchronizations
    in the DB are made manually not automatically

->  Bind=engine this is the one which is the bridge between the application 
    and the database as it the one which which involve the info
    about the db
"""