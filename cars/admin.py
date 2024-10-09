from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand') # aqui está dizendo que posso buscar tanto por carro quanto por marca


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)

