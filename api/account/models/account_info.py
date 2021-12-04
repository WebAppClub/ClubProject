from django.db import models

from . import User


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    first_name_reading = models.CharField(max_length=30)
    middle_name_reading = models.CharField(max_length=30, blank=True, null=True)
    last_name_reading = models.CharField(max_length=30)

    accept_newsletter = models.BooleanField(default=False, null=True, blank=True)

    money = models.PositiveIntegerField(default=0, null=False, blank=True)
    all_paid = models.PositiveIntegerField(default=0, null=False, blank=True)

    tel = models.TextField(default=None, null=True, blank=True)

    birthday = models.DateField(default=None, null=True, blank=True)

    address_level_1 = models.TextField(default=None, null=True, blank=True)
    address_level_2 = models.TextField(default=None, null=True, blank=True)
    address_line_1 = models.TextField(default=None, null=True, blank=True)
    address_line_2 = models.TextField(default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self, reading=False) -> str:
        if reading:
            if self.middle_name_reading is None:
                return " ".join([self.first_name_reading, self.last_name_reading])
            else:
                return " ".join(
                    [
                        self.first_name_reading,
                        self.middle_name_reading,
                        self.last_name_reading,
                    ]
                )
        else:
            if self.middle_name is None:
                return " ".join([self.first_name, self.last_name])
            else:
                return " ".join([self.first_name, self.middle_name, self.last_name])

    def get_user_address(self, in_list=False) -> str or list:
        address_list = [
            self.address_level_1,
            self.address_level_1,
            self.address_line_1,
            self.address_line_2,
        ]

        address_list = [address for address in address_list if not address is None]

        if in_list:
            return address_list
        else:
            return " ".join(address_list)

    def __str__(self):
        return f"{self.get_full_name()} - [{self.user_id}]"
