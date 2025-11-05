from .celery_app import celery
import time

@celery.task(bind=True)
def send_email_task(self, email: str):
    # Simulate heavy work
    time.sleep(2)
    print(f"Sending email to: {email}")
    return {"status": "sent", "email": email}