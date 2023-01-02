"""junchive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fake_gundori/', include('fake_gundori.urls')),
    path('blog/', include('blog.urls')),
    path('home/', include('homepage.urls')),
    path('', RedirectView.as_view(url='/fake_gundori/soldier', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # CSS, JavaScript, Image와 같은 Static Files 제공 가능하게 함
