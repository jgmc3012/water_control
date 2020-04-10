from django.urls import include, path

urlpatterns = [
    path('consumption-histories/', include('consumption_histories.routes')),
    path('measurers/', include('measurers.routes')),
    path('family-bosses/', include('family_bosses.routes')),
    path('houses/', include('houses.routes')),
    path('invoices/', include('invoices.routes')),
]
