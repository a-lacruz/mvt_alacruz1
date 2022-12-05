from django.contrib import admin
from django.urls import path
from app_desafio.views import listar_familiar


urlpatterns = [
    path('', listar_familiar),
]