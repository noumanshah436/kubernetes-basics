from fastapi import APIRouter
from app.worker.tasks import send_email_task

router = APIRouter()

@router.post("/send-email")
def send_email(email: str):
    task = send_email_task.delay(email)
    return {"task_id": task.id, "status": "queued"}