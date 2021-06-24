from django.shortcuts import render
from django.http import HttpResponseRedirect

from store.models import Order
from store.models import ShippingAddress
from store.models import OrderItem
from store.forms import ShippingForm, ServiceForm
# Create your views here.


def orders(request):
    order = Order.objects.all()
    item = OrderItem.objects.all()
    address = ShippingAddress.objects.all()
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'crm/orders.html', context)


def shipping(request):
    order = Order.objects.all()
    item = OrderItem.objects.all()
    address = ShippingAddress.objects.filter(status='Pending')
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'crm/shipping.html', context)


def pickTicket(request):
    order = Order.objects.all()
    item = OrderItem.objects.order_by('location')
    address = ShippingAddress.objects.filter(status='Pending')
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'crm/pickTicket.html', context)

def updateOrder(request, pk):
    address = ShippingAddress.objects.get(id=pk)
    form = ShippingForm(request.POST or None, instance=address)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'address': address, 'form':form}
    return render(request, 'CRM/updateOrder.html', context)

def serviceOrder(request, pk):
    address = ShippingAddress.objects.get(id=pk)
    form = ServiceForm(request.POST or None, instance=address)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'address': address, 'form':form}
    return render(request, 'CRM/serviceOrder.html', context)


def service(request):
    order = Order.objects.all()
    item = OrderItem.objects.all()
    address = ShippingAddress.objects.all()
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'crm/service.html', context)