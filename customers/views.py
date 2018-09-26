from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

class CustomerPurchaseLog(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer