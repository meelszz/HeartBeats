"""doc string"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('termsofservice', views.termsofservice, name='terms of service'),
    path('privacypolicy', views.privacypolicy, name='privacy policy'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)