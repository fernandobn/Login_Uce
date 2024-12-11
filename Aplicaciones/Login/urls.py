from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),  # Ruta para mostrar el formulario de login
    path('guardar_login/', views.guardar_login),  # Ruta para procesar el formulario
]
