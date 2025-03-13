from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='prontuarios'),  # Página inicial
]

