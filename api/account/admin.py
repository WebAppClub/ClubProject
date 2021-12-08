from django.contrib import admin

# Register your models here.
from .models import *

# Accountモデル
admin.site.register(User)
admin.site.register(Info)
admin.site.register(Permission)
