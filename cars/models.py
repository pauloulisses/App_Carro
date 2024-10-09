from django.db import models

# aqui onde vai escrever nosso modelos as tabelas do BD

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):

    id = models.AutoField(primary_key=True) 
    model = models.CharField(max_length=200) # modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # ano modelo do carro
    plate = models.CharField(max_length=10, blank=True, null=True) # placa dos carros
    value = models.FloatField(blank=True, null=True) # valor do carro
    photo = models.ImageField(upload_to='cars/',blank=True, null=True) # manipulação de imagens 

    def __str__(self):
        return self.model # aqui para retorna o modelo do carro

