from celery import shared_task
from .service import subtract_hold_from_balance


@shared_task()
def task_subtract_hold_from_balance(account_uuid):
    subtract_hold_from_balance(account_uuid)
