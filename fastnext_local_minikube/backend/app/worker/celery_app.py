import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

broker = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery = Celery("app.worker", broker=broker, backend=backend)
celery.conf.task_track_started = True