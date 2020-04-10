from django.urls import path

from . import views

app_name = 'invoices'

urlpatterns = [
    path('year/<int:year>/', views.InvoiceListView.as_view(), name='list'),
    path('year/<int:year>/month/<int:month>/', views.InvoiceListView.as_view(), name='list'),
    path('year/<int:year>/month/<int:month>/day/<int:day>/', views.InvoiceListView.as_view(), name='list'),
]