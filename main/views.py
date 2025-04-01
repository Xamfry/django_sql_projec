"""
Логика обработки запросов:
Принимают HTTP-запросы
Возвращают HTTP-ответы
Могут взаимодействовать с моделями и шаблонами
"""

from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def home(request):
    return render(request, 'main/index.html', {'title': 'Главная'})
# Create your views here.
