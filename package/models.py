from django.db import models

from destiny.models import Destiny

# Create your models here.
class Data_Package_One(models.Model):
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    date_arrive = models.DateField('Data da Chegada', default='01/01/2022')
    date_departure = models.DateField('Data da Partida', default='31/01/2022')
    num_adults = models.IntegerField('Quantidade adultos', default=2)
    num_child =  models.IntegerField('Quantidade crianças', default='0')
    name = models.CharField('Seu nome', max_length=200)
    email = models.EmailField('E-mail para contato', max_length=254)
    phonenumber = models.CharField('Telefone para contato', max_length=13)
    city = models.CharField('Cidade', max_length=100, null=True)
    description = models.TextField('Descrição', blank=True) 

    class Meta:
        verbose_name = "Pacote"
        verbose_name_plural = "Pacotes"


class Child_Package_One(models.Model):
    data_package_one = models.ForeignKey(Data_Package_One, on_delete=models.CASCADE)
    children_age = models.CharField('', max_length=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "Idade da criança"
        verbose_name_plural = "Idade das crianças"


# class Data_Customer_Package(models.Model):
#     package = models.OneToOneField(Data_Package_One, on_delete=models.CASCADE)
#     name = models.CharField('Seu nome', max_length=200)
#     email = models.EmailField('E-mail para contato', max_length=254)
#     phonenumber = models.CharField('Telefone para contato', max_length=13)
#     city = models.CharField('Cidade', max_length=100, null=True)
#     description = models.TextField('Descrição', blank=True)  

#     class Meta:
#         verbose_name = "Dados do cliente para pacote"
#         verbose_name_plural = "Dados do cliente para pacote"

#     def __str__(self):
#         return self.name +'-'+ self.package.destiny