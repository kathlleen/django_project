from django.db import models

# Create your models here.
from django.db import models

# from user.models import User
from goods.models import Products

from users.models import User


# Create your models here.

class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timeslape = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects = CartQueryset().as_manager()
    def __str__(self): # перегружаем для отображения названия в бд
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'

    def product_price(self):
        return self.product.price * self.quantity