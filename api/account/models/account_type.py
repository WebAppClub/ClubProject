from django.db import models

from .account_permission import Permission

class Type(models.Model):
    account_type = models.OneToOneField(Permission, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
