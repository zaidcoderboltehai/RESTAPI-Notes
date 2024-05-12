from rest_framework import serializers
from .models import User,Accounts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # user_accounts=serializers.StringRelatedField(many=True)
    # user_accounts=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    user_accounts=serializers.HyperlinkedIdentityField(many=True,view_name="accounts-detail")
    # user_accounts=serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='account_no'
    # )
    class Meta:
        model=User
        fields=["url","id","name","age","email","password","user_accounts"]

class AccountSerializer(serializers.ModelSerializer):
    user=UserSerializer(required=False,read_only=True)
    user_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Accounts 
        fields=["id","bank_name","account_no","user","user_id"]

    def create(self,validated_data):
        user_id=validated_data.pop('user_id')
        user=User.objects.get(pk=user_id)
        account=Accounts.objects.create(user=user, **validated_data)
        return account

