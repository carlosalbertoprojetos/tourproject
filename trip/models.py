from company.models import Company
from django.db import models
from season.models import Validity


class Categories(models.Model):
    name = models.CharField('Categoria', max_length=255, unique=True)
    slug = models.SlugField(max_length=250)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField('Nome', max_length=255,)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(
        'Imagem do produto', upload_to="produtos/%Y", blank=True)
    trip_description = models.TextField('Descrição do passeio', blank=True)
    short_description = models.TextField('Descrição curta', blank=True)
    
    politic = models.CharField('Política de CHD', max_length=255)
    trip_duration = models.CharField('Duração do passeio', max_length=255)
    
    travel_time = models.CharField('Tempo de percurso', max_length=255)
    travel_time_untoplace = models.CharField('Tempo de percurso até o local do passeio', max_length=255)
    
    ride_distance = models.CharField('Distância do passeio', max_length=255)
    limit_load = models.CharField('Limite de carga por passeio ou guia', max_length=255)
    commission = models.DecimalField('Comissão paga pelo fornecedor', max_digits=5, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Categoria')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    tour_notes = models.TextField('Notas do passeio', blank=True)
    featured_image = models.FileField('Imagem de destaque para o site', upload_to='files/')
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Passeio"
        verbose_name_plural = "Passeios"

    def __str__(self):
        return self.name
    
    
class CategoriesPax(models.Model):
    name = models.CharField('Categoria PAX', max_length=255)

    def __str__(self):
        return self.name


class TripSeasonPrices(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, verbose_name='Passeio')
    validity = models.ForeignKey(Validity, on_delete=models.DO_NOTHING, verbose_name='Vigência')
    cadpax = models.ForeignKey(CategoriesPax, on_delete=models.DO_NOTHING, verbose_name='Cadastro PAX')
    price = models.CharField('Preço', max_length=9)

    def __str__(self):
        return self.trip +' - '+ self.validity +' - '+ self.cadpax + ' - R$ ' + self.price
