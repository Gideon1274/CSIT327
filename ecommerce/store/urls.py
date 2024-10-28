from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.login_view, name="login_view"),
    path('logout/',views.user_logout,name='logout'),
    path('signup/', views.signup_view, name='signup_view'), 

    path('search/', views.search_view, name='search_view'),
]
