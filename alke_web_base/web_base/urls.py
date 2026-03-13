from django.urls import path
from . import views

urlpatterns = [
    # Esta línea hace que al entrar a http://127.0.0.1:8000/ se vea el Login
    path('', views.login_view, name='login'), 
    
    path('menu/', views.menu_view, name='menu'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('send-money/', views.send_money_view, name='send_money'),
    path('transactions/', views.transactions_view, name='transactions'),
]