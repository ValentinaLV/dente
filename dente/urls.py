"""dente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index, about, contact, news, feedback, service, price_list

urlpatterns = [
    path('', index, name='home_page'),
    path('about/', about, name='about_page'),
    path('contact/', contact, name='contact_page'),
    path('news/', news, name='news_page'),
    path('feedback/', feedback, name='feedback_page'),
    path('service/', service, name='service_page'),
    path('pricing/', price_list, name='price_list_page'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
