from django.db import models

from destiny.models import Destiny

# Create your models here.
class Data_Package_One(models.Model):
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    date_arrive = models.DateField('Data da Chegada')
    date_departure = models.DateField('Data da Partida')
    num_adults = models.IntegerField('Quantidade adultos')
    num_child =  models.IntegerField('Quantidade crianças')


class Child_Package_One(models.Model):
    data_package_one = models.ForeignKey(Data_Package_One, on_delete=models.CASCADE)
    children_age = models.CharField('', max_length=2)