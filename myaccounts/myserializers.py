from rest_framework.serializers import ModelSerializer
from mydatabases.models import UserDatas

class AccountSerializer(ModelSerializer):
    class Meta:
        model=UserDatas
        fields = '__all__'

class UserSeeSerializer(ModelSerializer):
    class Meta:
        model=UserDatas
        fields = ['usernameAccount', 'emailAccount', 'emailAuth', 'walletAddress', 'evaluation']