from django.urls import path, include
from .views import Register
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]