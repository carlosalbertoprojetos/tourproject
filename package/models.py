from django.db import models

from destiny.models import Destiny
from trip.models import ActivityPrice 


class Package(models.Model):
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    date_arrive = models.DateField('Data da Chegada', default='01/01/2022')
    date_departure = models.DateField('Data da Partida', default='01/12/2022')
    num_adults = models.IntegerField('Quantidade adultos', default=2)
    num_child =  models.IntegerField('Quantidade crianças', default=0)
    name = models.CharField('Seu nome', max_length=200)
    email = models.EmailField('E-mail para contato', max_length=255)
    phonenumber = models.CharField('Telefone para contato', max_length=15)
    city = models.CharField('Cidade', max_length=100, null=True)
    description = models.TextField('Descrição', blank=True) 

    class Meta:
        verbose_name = "Pacote"
        verbose_name_plural = "Pacotes"

class Child_Package_One(models.Model):
    data_package_one = models.ForeignKey(Package, on_delete=models.CASCADE)
    children_age = models.CharField('', max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = "Idade da criança"
        verbose_name_plural = "Idade das crianças"

class PackageTrips(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    id_price = models.ForeignKey(ActivityPrice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Atividade do pacote"
        verbose_name_plural = "Atividades do Pacote"
