from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('customer_form',views.customer_form,name='customer_form'),
    path('logout',views.logout,name="logout")
]
