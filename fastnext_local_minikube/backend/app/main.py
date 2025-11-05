from fastapi import FastAPI
from app.api import users, tasks
from app.db.database import engine, Base

app = FastAPI(title="FastNext Local")

# create tables (for demo only)
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "FastAPI backend running"}