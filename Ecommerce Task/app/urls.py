from django.urls import path
from . import views

urlpatterns = [
     path('', views.home ,name='home'),
     path('about/', views.about ,name='about'),
     path('blog_details/', views.blog_details ,name='blog_details'),
     path('contact/', views.contact ,name='contact'),
     path('footer/', views.footer ,name='footer'),
     path('header/', views.header ,name='header'),  
     path('shop/', views.shop ,name='shop'),
     path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
     path('shop_details/', views.shop_details, name='shop_details'),
     path('checkout/', views.checkout, name='checkout'),
     path('blog/', views.blog, name='blog'),
     
]