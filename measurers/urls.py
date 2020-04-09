from django.urls import path

from . import views

app_name = 'measurers'

urlpatterns = [
    path('actualizar/', views.visual_update, name='visual_update')
]