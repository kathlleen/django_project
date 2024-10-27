from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.db import transaction
from django.contrib import messages

from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order
from orders.models import OrderItem


# Create your views here.
def create_order(request):

    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic(): # атомарные транзакции
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number = form.cleaned_data['phone_number'],
                            requires_delivery = form.cleaned_data['requires_delivery'],
                            delivery_address = form.cleaned_data['delivery_address'],
                            payment_on_get = form.cleaned_data['payment_on_get']
                        )
                        # создать заказанные товары (orderItem)
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                      В наличии = {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                            product.quantity -= quantity
                            product.save()

                        # очистить корзину после заказа
                        cart_items.delete()

                        return redirect('user:profile')

            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('orders:create_order')

    else:
        initial = {
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            }

        form = CreateOrderForm(initial=initial) # изначальные данные

    context = {
        'title' : 'Оформление заказа',
        'form' : form,
    }

    return render(request, 'orders/create_order.html', context=context)