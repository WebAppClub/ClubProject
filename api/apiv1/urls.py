from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('account/register/', views.RegisterView.as_view(), name='account_register'),
]
