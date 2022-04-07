from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from shop.models import Order

def customer_list(request):
    users = User.objects.all()
    return render(request, 'shop/customer_list.html', {'users': users})

def customer_detail(request, id):
    user = get_object_or_404(User, id=id)
    orders = Order.objects.filter(customer_id=id)
    return render(request, 'shop/customer_detail.html', {'user': user, 'orders': orders})

