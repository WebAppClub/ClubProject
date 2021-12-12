from rest_framework import serializers

from account.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "account_permission",
            "last_login",
            "date_joined",
            "is_deleted",
            "is_verified",
            "created_at",
            "updated_at",
        ]
