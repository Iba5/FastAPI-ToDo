from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers.TaskController import router as paths
from db.sessions import *


@asynccontextmanager
async def lifespan(apk: FastAPI):
    print("Starting up...")
    create_db()   # create tables on startup
    yield
    print("Shutting down...")
    engine.dispose()  # close connection pool


apk= FastAPI(lifespan=lifespan,title="To Do List", description="The To Do List App")
apk.include_router(paths)




"""
We will be wanting the db to be established on the start of the
application which mean that we are going to create an instance of 
the engine here in the main
"""