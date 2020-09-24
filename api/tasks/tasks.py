from celery import shared_task
from .service import subtract_hold_from_balances


@shared_task()
def task_subtract_hold_from_balances():
    subtract_hold_from_balances()
