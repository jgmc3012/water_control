from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'houses'

urlpatterns = [
    path('', views.HouseViewListCreate.as_view(), name='list_create'),
    path('<int:pk>/', views.HouseDetailView.as_view(), name='detail'),
]