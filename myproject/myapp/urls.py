from django.urls import path
from .views import index, about, site_settings, contact


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('site_settings/', site_settings, name='site_settings'),
    path('contact/', contact, name='contact'),
]
