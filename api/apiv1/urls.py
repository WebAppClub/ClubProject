from django.urls import path, include

from .views import sendmail

app_name = 'apiv1'

urlpatterns = [
    path('test/', sendmail, name='test'),
]
