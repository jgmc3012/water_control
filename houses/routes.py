from django.urls import path
from . import views

app_name = 'houses'

urlpatterns = [
    path('', views.HouseViewListCreate.as_view(), name='list_create'),
    path('<int:pk>/', views.HouseDetailView.as_view(), name='detail'),
]