from common.models import Account


def subtract_hold(account):
    account.balance -= account.hold
    account.hold = 0
    account.save()


def subtract_hold_from_balances():
    accounts = Account.objects.all()
    for account in accounts:
        subtract_hold(account)
