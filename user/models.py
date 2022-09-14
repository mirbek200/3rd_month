from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.user}'


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isVendor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'