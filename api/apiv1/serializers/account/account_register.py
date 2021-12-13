from account.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from account.models.account_permission import Permission

import datetime


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(write_only=True, required=True)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    checkPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'checkPassword')

    def validate(self, attrs):
        if attrs['password'] != attrs['checkPassword']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            last_login=datetime.datetime.now(JST),
            account_permission=Permission.objects.get(pk=1),
            is_deleted=False,
            is_verified=False
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
