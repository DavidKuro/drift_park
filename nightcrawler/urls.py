from django.urls import path
from .import views

urlpatterns =[
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.product, name='product'),
    path('checkout',views.checkout, name='checkout'),
    path('product',views.product, name='product'),
    path('blog',views.blog, name='blog'),
    path('cart',views.cart, name='cart')
]