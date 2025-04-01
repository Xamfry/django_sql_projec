from django.apps import AppConfig # type: ignore


class ShopCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_core'
    verbose_name = "Основное приложение"
