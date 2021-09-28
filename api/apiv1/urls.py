from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserView

router = DefaultRouter()
# router.register(r'jwt/user', obtain_jwt_token)
# router.register(r'^jwt/refresh/', refresh_jwt_token)
# router.register(r'^jwt/verify/', verify_jwt_token)

urlpatterns = [
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
    path('jwt/verify/', verify_jwt_token),
    path('jwt/me/', UserView.as_view()),
]
