from rest_framework.exceptions import APIException


class AccountNotActiveException(APIException):
    status_code = 400
    default_detail = 'Аккаунт неактивен'
    default_code = 'account_inactive'


class SubtractIsNotPossible(APIException):
    status_code = 400
    default_detail = 'Недостаточно средств'
    default_code = 'not_enough_money'
