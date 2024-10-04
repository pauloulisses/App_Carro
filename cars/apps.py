from django.apps import AppConfig

# Trás configurações do nosso app que é cars
class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
