from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator

from accounts.models import *
from accounts.forms import OrderForm, CreateUserForm, CustomerForm, ProductForm, TagForm
from accounts.filters import CustomerOrderFilter, OrderFilter

# Orders
@login_required(login_url='login')
def orders(request):
    orders = Order.objects.all().order_by("-date_created")

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
# Paginator
    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    context = {'orders': orders, 
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending, 'myFilter': myFilter}
    return render(request, 'orders/orders.html', context)


@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'orders/order_create.html', context)


@login_required(login_url='login')
def createOrderCustomer(request, pk):
    orderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status', 'quantity'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = orderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = orderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset, 'customer': customer}
    return render(request, 'orders/order_form_customer.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'orders/order_update.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'orders/order_delete.html', context)

