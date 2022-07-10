from django.db import models

from destiny.models import Destiny

# Create your models here.
class Data_Package_One(models.Model):
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    date_arrive = models.DateField('Data da Chegada')
    date_departure = models.DateField('Data da Partida')
    num_adults = models.IntegerField('Quantidade adultos')
    num_child =  models.IntegerField('Quantidade crianças')

    class Meta:
        verbose_name = "Pacote"
        verbose_name_plural = "Pacotes"


class Child_Package_One(models.Model):
    data_package_one = models.ForeignKey(Data_Package_One, on_delete=models.CASCADE)
    children_age = models.CharField('', max_length=2)
    
    class Meta:
        verbose_name = "Idade da criança"
        verbose_name_plural = "Idades das crianças"


# class Data_Package_Two(models.Model):


#     class Meta:
#         verbose_name = "Pacote"
#         verbose_name_plural = "Pacotes"