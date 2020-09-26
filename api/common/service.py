from common.exceptions import SubtractIsNotPossible
from tasks.tasks import task_subtract_hold_from_balance
from datetime import datetime, timedelta


def add_balance_to_account(account, add):
    """
    Добавление средств на счет.

    :param account: Объект счета.
    :param add: Сумма добавления.
    :return: Объект счета или исключение (если счет неактивен).
    """

    account.balance += add
    account.save()
    return account


def check_if_possible_to_subtract_balance(account, subtraction):
    """
    Проверка - возможен ли вычет со счета.

    :param account: Объект счета.
    :param subtraction: Сумма вычета.
    :return: Баланс после вычета или исключение (если после вычета баланс на счете будет меньше нуля).
    """

    new_balance = account.balance - account.hold - subtraction
    if new_balance < 0:
        raise SubtractIsNotPossible()
    return True


def add_hold(account, hold):
    if check_if_possible_to_subtract_balance(account, hold):
        account.hold += hold
        account.save()
        return account


def subtract_from_account_balance(account, subtraction):
    """
    Вычитание из баланса значения balance.

    :param account: Объект счета.
    :param subtraction: Сумма вычета.
    :return: Объект счета или исключение (если баланс после вычета на счете будет меньше нуля).
    """

    account = add_hold(account, subtraction)
    task_subtract_hold_from_balance.apply_async(args=(account.uuid,), eta=datetime.utcnow() + timedelta(minutes=10))
    return account
