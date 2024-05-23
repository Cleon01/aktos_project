from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer

class AccountListView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        print("get_queryset called")  # Debugging line
        queryset = Account.objects.all()
        min_balance = self.request.query_params.get('min_balance')
        max_balance = self.request.query_params.get('max_balance')
        consumer_name = self.request.query_params.get('consumer_name')
        status = self.request.query_params.get('status')

        if min_balance is not None:
            queryset = queryset.filter(balance__gte=min_balance)
        if max_balance is not None:
            queryset = queryset.filter(balance__lte=max_balance)
        if consumer_name is not None:
            queryset = queryset.filter(consumers__name__icontains(consumer_name))
        if status is not None:
            queryset = queryset.filter(status=status)

        print(queryset)  # Debugging line
        return queryset