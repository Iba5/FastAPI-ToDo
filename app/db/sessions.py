from sqlalchemy.orm.session import sessionmaker
from .connections import engine

sessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
SessionMaker:
->  This is the icing to the cake, It is the one which finalises
    the db to app connection as it is the one responsible for 
    communicating or converting from py to sql 
->  When we set autocommit to false we telling it
    to not update or do anything unless we
    tell it to do so
    autoflash is also set to false so as to tell the db
    that it should not remove anything unless the user 
    permits it to do so
->  Bind=engine this is the one which is the bridge between the application 
    and the database as it the one which which involve the info
    about the db
"""