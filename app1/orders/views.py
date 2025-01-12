from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order
from orders.models import OrderItem


# Create your views here.


class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm

    succes_url = reverse_lazy('user:profile')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        try:
            with transaction.atomic():  # атомарные транзакции
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    # создать заказ
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get']
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
            messages.error(self.request, str(e))
            return redirect('orders:create_order')

    def form_invalid(self):
        return redirect('orders:create_order')

    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['order'] : True
        return context

# @login_required
# def create_order(request):
#
#     if request.method == 'POST':
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic(): # атомарные транзакции
#                     user = request.user
#                     cart_items = Cart.objects.filter(user=user)
#
#                     if cart_items.exists():
#                         # создать заказ
#                         order = Order.objects.create(
#                             user=user,
#                             phone_number = form.cleaned_data['phone_number'],
#                             requires_delivery = form.cleaned_data['requires_delivery'],
#                             delivery_address = form.cleaned_data['delivery_address'],
#                             payment_on_get = form.cleaned_data['payment_on_get']
#                         )
#                         # создать заказанные товары (orderItem)
#                         for cart_item in cart_items:
#                             product = cart_item.product
#                             name = cart_item.product.name
#                             price = cart_item.product.sell_price()
#                             quantity = cart_item.quantity
#
#                             if product.quantity < quantity:
#                                 raise ValidationError(f'Недостаточное количество товара {name} на складе\
#                                                       В наличии = {product.quantity}')
#
#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#
#                             product.quantity -= quantity
#                             product.save()
#
#                         # очистить корзину после заказа
#                         cart_items.delete()
#
#                         return redirect('user:profile')
#
#             except ValidationError as e:
#                 messages.error(request, str(e))
#                 return redirect('orders:create_order')
#
#     else:
#         initial = {
#             'first_name' : request.user.first_name,
#             'last_name' : request.user.last_name,
#             }
#
#         form = CreateOrderForm(initial=initial) # изначальные данные
#
#     context = {
#         'title' : 'Оформление заказа',
#         'form' : form,
#         'order' : True,
#     }
#
#     return render(request, 'orders/create_order.html', context=context)