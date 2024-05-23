from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Client, Consumer, Account

class AccountTests(TestCase):
    def setUp(self):
        client = Client.objects.create(name='Client A')
        consumer1 = Consumer.objects.create(name='John Doe')
        consumer2 = Consumer.objects.create(name='Jane Doe')
        account = Account.objects.create(client=client, balance=500, status='in_collection')
        account.consumers.add(consumer1, consumer2)

    def test_account_list(self):
        response = self.client.get('/api/accounts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)