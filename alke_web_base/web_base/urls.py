from django.urls import path
from . import views

urlpatterns = [
    path('',              views.login_view,       name='login'),
    path('menu/',         views.menu_view,        name='menu'),
    path('deposit/',      views.deposit_view,     name='deposit'),
    path('send-money/',   views.send_money_view,  name='send_money'),
    path('add-contact/',  views.add_contact_view, name='add_contact'),
    path('transactions/', views.transactions_view, name='transactions'),
]