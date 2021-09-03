from django.urls import path, include
from rest_framework.routers import DefaultRouter


# ルーティング
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls))
]
