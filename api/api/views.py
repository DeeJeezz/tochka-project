from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from common.models import Account
from common import serializers


def error404(request, exception):
    # return Response()
    response_data = {}
    response_data['detail'] = 'Not found.'
    return NotFound()


@api_view(['GET'])
def ping(request):
    return Response({'status': 'pong'})


class AccountListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Список счетов.
    """

    queryset = Account.objects.all()
    serializer_class = serializers.AccountListSerializer


class AccountDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Информация о выбранном счете.
    """

    queryset = Account.objects.filter()
    serializer_class = serializers.AccountDetailSerializer


class AccountAddBalanceViewSet(viewsets.ModelViewSet):
    """
    Пополнение баланса.
    """

    queryset = Account.objects.filter()
    serializer_class = serializers.AccountAddBalanceSerializer


class AccountSubtractBalanceViewSet(viewsets.ModelViewSet):
    """
    Уменьшение баланса (увеличение холда).
    """

    queryset = Account.objects.filter()
    serializer_class = serializers.AccountSubtractBalanceSerializer
