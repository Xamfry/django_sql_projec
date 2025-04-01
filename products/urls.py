"""
Маршрутизация URL:
Сопоставляет URL-адреса с представлениями
Может включать URL-паттерны из других приложений
"""

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]