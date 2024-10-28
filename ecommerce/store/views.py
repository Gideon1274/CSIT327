from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required




def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('store:login_view') 
        else:
            messages.error(request, "Error creating account. Please try again.")
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('/store')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {'form': form})


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()  # Fetch all products
    context = {'products': products, 'cartItems': cartItems}  # Pass products to the context
    return render(request, 'store/store.html', context)  # Render store.html with the context


@login_required
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


@login_required
def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


# from django.view.decorators.csrf import csrf_exempt
# @csrf_exempt

@login_required
def processOrder(request):
    # print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment complete!', safe=False)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

from django.shortcuts import render
from .models import Product, Category  # Adjust based on your models

@login_required
def search_view(request):
    categories = Category.objects.all()  # Fetch all categories
    selected_category = request.GET.get('category', None)
    query = request.GET.get('query', '')

    products = Product.objects.all()
    if selected_category:
        products = products.filter(category_id=selected_category)  # Filter by selected category
    if query:
        products = products.filter(name__icontains=query)  # Filter by query

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'products': products,
        'cartItems': cartData(request)['cartItems'],  # Ensure cartItems are included
    }
    return render(request, 'store/store.html', context)  # Render store.html with the context


from django.shortcuts import render
from .models import Product  # Assuming Product is your model

# def store_view(request):
#     query = request.GET.get('query', '')
#     category_id = request.GET.get('category', '')

#     products = Product.objects.all()  # Get all products by default

#     if category_id:
#         products = products.filter(category_id=category_id)  # Filter by selected category

#     if query:
#         products = products.filter(name__icontains=query)  # Filter by search term

#     categories = Category.objects.all()  # Assuming you have a Category model
#     context = {
#         'products': products,
#         'categories': categories,
#     }

#     return render(request, 'store/store.html', context)


@login_required
def store(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()

    if category_id:
        products = products.filter(category__id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'store/store.html', {'products': products})