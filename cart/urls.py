"""
Маршрутизация URL:
Сопоставляет URL-адреса с представлениями
Может включать URL-паттерны из других приложений
"""

from django.urls import path # type: ignore
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/<int:product_id>/', views.add, name='add'),
]