"""water_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('water_control.routes')),
    path('jefes-de-familia/', include('family_bosses.urls')),
    path('casas/', include('houses.urls')),
    path('medidores/', include('measurers.urls')),
    path('recibos/', include('invoices.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

