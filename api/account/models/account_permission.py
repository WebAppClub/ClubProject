from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    is_can_open_admin = models.BooleanField(default=False, null=False, blank=True)

    is_can_buy = models.BooleanField(default=False, null=False, blank=True)
    is_can_sell = models.BooleanField(default=False, null=False, blank=True)

    is_can_create_account_permission = models.BooleanField(default=False, null=False, blank=True)
    is_can_delete_account_permission = models.BooleanField(default=False, null=False, blank=True)

    is_can_delete_account = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self):
        return f"{self.name}"
