from fastapi import FastAPI
from app.controllers.TaskController import router as paths 

app= FastAPI(title="To Do List", description="The To Do List App")
app.include_router(paths)