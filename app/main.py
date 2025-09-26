from fastapi import FastAPI
from controllers.TaskController import router as paths 

apk= FastAPI(title="To Do List", description="The To Do List App")
apk.include_router(paths)