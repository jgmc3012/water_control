from django.urls import path

from . import views

app_name = 'measurers_visual'

urlpatterns = [
    path('actualizar/', views.visual_update, name='update')
]