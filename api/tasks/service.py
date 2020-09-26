from common.models import Account
from django.db import transaction


def subtract_hold_from_balance(account_uuid):
    account = Account.objects.get(pk=account_uuid)

    with transaction.atomic():
        account.balance -= account.hold
        account.hold = 0
        account.save()
