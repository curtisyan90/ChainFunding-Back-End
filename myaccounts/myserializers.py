from rest_framework.serializers import ModelSerializer
from mydatabases.models import UserDatas

class AccountSerializer(ModelSerializer):
    class Meta:
        model=UserDatas
        fields = '__all__'