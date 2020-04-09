from django.urls import path

from . import views

app_name = 'family_bosses_visual'

urlpatterns = [
    path('crear/', views.visual_create, name='create')
]