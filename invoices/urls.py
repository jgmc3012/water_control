from django.urls import path

from . import views

app_name = 'invoices_visual'

urlpatterns = [
    path('nuevo-pago', views.visual_pay, name='pay')
]