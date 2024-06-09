from django.urls import path
from . import views

urlpatterns = [
    # path('', views.payment_view, name='payment_view'),
    path('pay/', views.pay, name='pay'),
]