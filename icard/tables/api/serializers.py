from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from tables.models import Table
from users.api.serializers import UserSerializer

class TableSerializer(ModelSerializer):
    waiter_data = UserSerializer(source='waiter', read_only=True)
    class Meta:
        model = Table
        fields = ['id', 'number', 'waiter', 'waiter_data']
