from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from common.models import Account


class AccountTests(APITestCase):
    def setUp(self):
        self.test_account = Account.objects.create(
            fio='Test_fam Test_name Test_otch', balance=1000, hold=200, status=True
        )

    def test_get_status(self):
        url = reverse('status', kwargs={'pk': self.test_account.uuid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'balance': 1000, 'status': True})

    def test_add_balance(self):
        url = reverse('add', kwargs={'pk': self.test_account.uuid})
        data = {'balance': 1200}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'balance': 2200})
        self.assertEqual(Account.objects.get().balance, 2200)

    def test_check_for_subtract_error(self):
        url = reverse('subtract', kwargs={'pk': self.test_account.uuid})
        data = {'hold': 5000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('errors', {}).get('code'), 'not_enough_money')
        self.assertEqual(Account.objects.get().hold, 200)

    def tearDown(self):
        self.test_account.delete()
