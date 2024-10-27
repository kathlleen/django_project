# Register your models here.
from django.contrib import admin
from carts.admin import CartTabAdmin
# Register your models here.

from .models import User
from orders.admin import OrderTabulareAdmin


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']
    inlines = [CartTabAdmin, OrderTabulareAdmin]