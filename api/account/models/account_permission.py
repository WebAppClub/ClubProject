from django.db import models

class Permission(models.Model):
    is_can_open_admin = models.BooleanField(default=False, null=False, blank=True)

    is_can_buy = models.BooleanField(default=False, null=False, blank=True)
    is_can_sell = models.BooleanField(default=False, null=False, blank=True)

    is_can_create_account_type = models.BooleanField(default=False, null=False, blank=True)
    is_can_delete_account_type = models.BooleanField(default=False, null=False, blank=True)

    is_can_create_account_permission = models.BooleanField(default=False, null=False, blank=True)
    is_can_delete_account_permission = models.BooleanField(default=False, null=False, blank=True)

    is_can_delete_account = models.BooleanField(default=False, null=False, blank=True)
