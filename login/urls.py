from django.urls import re_path
from .import views

# Asignar esas vistas a ciertas rutas dentro de urlpatterns
urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
]