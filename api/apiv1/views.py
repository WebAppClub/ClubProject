import datetime
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from django.utils.timezone import make_aware
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status, authentication, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response(status=HTTP_401_UNAUTHORIZED)

        return Response(
            data={
                "user": {
                    "id": request.user.id,
                    "username": request.user.username,
                    "email": request.user.email,
                }
            },
            status=status.HTTP_200_OK,
        )
