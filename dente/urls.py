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
from django.urls import path, include


urlpatterns = [
    path('', include(('aboutus.urls', 'aboutus'), namespace='about')),
    path('feedback/', include(('feedback.urls', 'feedback'), namespace='feedback')),
    path('news/', include(('news.urls', 'news'), namespace='news')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('pricing/', include(('pricing.urls', 'pricing'), namespace='pricing')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('subscribe/', include(('subscribe.urls', 'subscribe'), namespace='subscribe')),

    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
