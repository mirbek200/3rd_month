from django.contrib import admin

from apps.cart.models import Cart
from .models import PhoneNumber, Account

admin.site.register(PhoneNumber)
admin.site.register(Account)
admin.site.register(Cart)
