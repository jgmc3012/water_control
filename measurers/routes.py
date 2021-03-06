from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'measurers'

urlpatterns = [
    path('update/<str:house_id>/', views.MeasurerUpdate.as_view(), name='update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)