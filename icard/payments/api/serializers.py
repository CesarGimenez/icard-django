from rest_framework.serializers import ModelSerializer
from payments.models import Payment
from users.api.serializers import UserSerializer
from tables.api.serializers import TableSerializer

class PaymentSerializer(ModelSerializer):
    waiter_data = UserSerializer(source='waiter', read_only=True)
    table_data = TableSerializer(source='table', read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'table', 'table_data', 'waiter', 'waiter_data', 'totalPayment', 'paymentType', 'statusPayment', 'created_at']