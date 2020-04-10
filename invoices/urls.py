from django.urls import path

from . import views

app_name = 'invoices_visual'

urlpatterns = [
    path('pagar', views.visual_pay, name='pay'),
    path('listar', views.visual_list, name='list'),
]