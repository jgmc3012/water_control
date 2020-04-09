from django.urls import path

from . import views

app_name = 'invoices'

urlpatterns = [
    path('nuevo-pago', views.visual_new_pay, name='visual_new_pay')
]