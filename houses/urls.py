from django.urls import path

from . import views

app_name = 'houses_visual'

urlpatterns = [
    path('crear/', views.visual_create, name='create')
]