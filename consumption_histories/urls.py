from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'consumption_histories'

urlpatterns = [
    path('', views.ConsumptionHistoryListView.as_view(), name='list_or_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)