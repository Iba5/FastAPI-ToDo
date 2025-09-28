from fastapi import FastAPI
from controllers.TaskController import router as paths  


apk= FastAPI(title="To Do List", description="The To Do List App")
apk.include_router(paths)


"""
We will be wanting the db to be established on the start of the
application which mean that we are going to create an instance of 
the engine here in the main
"""