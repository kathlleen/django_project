from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Prefetch

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

from carts.models import Cart

from orders.models import Order, OrderItem


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            # if request.GET.get('next', None):
            #     return HttpResponseRedirect(request.POST.get('next'))

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserLoginForm()

    context = {
        'title' : "Authorization",
        'form': form,
    }
    return render(request, 'users/login.html',context)

def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()


    context = {
        'title' : "Registration",
        'form' : form
    }
    return render(request, 'users/registration.html',context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    'orderitem_set',
                    queryset=OrderItem.objects.select_related('product'),
                )
            )
            .order_by("-id")
    )

    context = {
        'title' : "Profile",
        'form' : form,
        'orders' : orders,
    }
    return render(request, 'users/profile.html',context)
@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))