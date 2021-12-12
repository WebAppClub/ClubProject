from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apiv1.serializers import AccountSerializer, InfoSerializer

from account.models import Info

class AccountView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = AccountSerializer

    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "account_permission": user.account_permission.id,
            "last_login": user.last_login,
            "date_joined": user.date_joined,
            "is_deleted": user.is_deleted,
            "is_verified": user.is_verified,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }

        if Info.objects.filter(user_id=user.id).exists():
            user_info = Info.objects.filter(user_id=user.id)[0]
            data["user_info"] = {
                "first_name": user_info.first_name,
                "middle_name": user_info.middle_name,
                "last_name": user_info.last_name,
                "first_name_reading": user_info.first_name_reading,
                "middle_name_reading": user_info.middle_name_reading,
                "last_name_reading": user_info.last_name_reading,
                "accept_newsletter": user_info.accept_newsletter,
                "money": user_info.money,
                "all_paid": user_info.all_paid,
                "tel": user_info.tel,
                "birthday": user_info.birthday,
                "address_level_1": user_info.address_level_1,
                "address_level_2": user_info.address_level_2,
                "address_line_1": user_info.address_line_1,
                "address_line_2": user_info.address_line_2,
                "created_at": user_info.created_at,
                "updated_at": user_info.updated_at
            }
        else:
            data["user_info"] = "Not Found."

        response = Response(data, status=status.HTTP_200_OK)
        return response
