from django.db import models

# aqui onde vai escrever nosso modelos as tabelas do BD

class Car(models.Model):

    id = models.AutoField(primary_key=True) 
    model = models.CharField(max_length=200) # modelo do carro
    brand = models.CharField(max_length=200) # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # ano modelo do carro
    value = models.FloatField(blank=True, null=True) # valor do carro



