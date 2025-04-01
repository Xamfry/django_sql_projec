"""
Логика обработки запросов:
Принимают HTTP-запросы
Возвращают HTTP-ответы
Могут взаимодействовать с моделями и шаблонами
"""

from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# def home(request):
#     return render(request, 'main/index.html', {'title': 'Главная'})

# Create your views here.

def detail(request):
    # Заглушка для примера
    context = {
        'cart_items': [
            {
                'product': {
                    'name': 'Пример товара',
                    'price': 1000,
                    # 'image': {'url': '/static/images/placeholder.jpg'}
                },
                'quantity': 2,
                'total_price': 2000
            }
        ],
        'total_price': 2000
    }
    return render(request, 'cart/detail.html', context)

def add(request, product_id):
    # Логика добавления в корзину
    pass