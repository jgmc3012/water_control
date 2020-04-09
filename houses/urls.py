from django.urls import path

from . import views

app_name = 'houses'

urlpatterns = [
    path('crear/', views.visual_create, name='visual_create')
]