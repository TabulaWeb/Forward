from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('addd/<int:product_id>/', views.cart_addd, name='cart_addd'),
    path('adddd/<int:product_id>/', views.cart_adddd, name='cart_adddd'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
