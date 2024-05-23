import csv
from django.core.management.base import BaseCommand
from accounts.models import Client, Consumer, Account

class Command(BaseCommand):
    help = 'Import accounts from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                client, _ = Client.objects.get_or_create(name=row['client reference no'])
                account, _ = Account.objects.get_or_create(
                    client=client,
                    balance=row['balance'],
                    status=row['status']
                )
                consumer_name = row['consumer name']
                consumer, _ = Consumer.objects.get_or_create(name=consumer_name.strip())
                account.consumers.add(consumer)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))