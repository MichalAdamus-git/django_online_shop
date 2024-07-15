from celery import shared_task

@shared_task(bind=True)
def home_converting(self):
    pass