from django.contrib import admin

from carts.models import Cart

# Register your models here.
#
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timeslape"
    search_fields = "product", "quantity", "created_timeslape"
    readonly_fields = ("created_timeslape",)
    extra = 1
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'quantity', 'created_timeslape']
    list_filter = ['created_timeslape', 'user', 'product__name']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Anonymys user"

