from company.models import Company
from django.db import models
from tinymce.models import HTMLField
from season.models import Season


class Categories(models.Model):
    name = models.CharField('Categoria', max_length=255, unique=True)
    slug = models.SlugField(max_length=250)
    description = HTMLField('Descrição', blank=True)

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
    trip_description = HTMLField('Descrição do passeio', blank=True)
    short_description = models.TextField('Descrição curta', blank=True)
    
    politic = models.PositiveIntegerField('Política de CHD')
    trip_duration = models.CharField('Duração do passeio (hrs)', max_length=255)
    
    travel_time = models.CharField('Tempo de percurso (hrs)', max_length=255)
    travel_time_untoplace = models.CharField('Tempo de percurso até o local do passeio', max_length=255)
    
    ride_distance = models.CharField('Distância do passeio (Km)', max_length=255)    
    limit_load = models.CharField('Limite de carga por passeio ou guia', max_length=255)    
    commission = models.DecimalField('Comissão paga pelo fornecedor', max_digits=5, decimal_places=2, blank=True, null=True)    
    category = models.ForeignKey(Categories, verbose_name='Categoria', on_delete=models.CASCADE)    
    company = models.ForeignKey(Company, verbose_name='Empresa',on_delete=models.CASCADE)    
    tour_notes = models.TextField('Notas do passeio', blank=True)    
    featured_image = models.FileField('Imagem de destaque para o site', upload_to='files/')
    seo = models.CharField('Dados para SEO', max_length=155)
    title = models.CharField('Título', max_length=150)
    description = HTMLField('Descrição', blank=True)
    description_BTMS = models.TextField('Vínculo ao sistema BTMS e Voucher Digital', max_length=300)    
    btms = models.CharField('Codigo BTMS', max_length=300)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Passeio"
        verbose_name_plural = "Passeios"

class CategoriesPax(models.Model):
    name = models.CharField('Categoria PAX', max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria PAX"
        

    def __str__(self):
        return self.name


class TripSeasonPrices(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, verbose_name='Passeio')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    cadpax = models.ForeignKey(CategoriesPax, on_delete=models.DO_NOTHING, verbose_name='Cadastro PAX')
    price = models.CharField('Preço', max_length=9)

    class Meta:
        ordering = ["trip"]
        verbose_name = "Preço Temporada de Passeio"
        

    def __str__(self):
        return self.trip
"""
Nome
Slug
Descrição do passeio
Short Description (máximo 200 caracteres)

Política de CHD
Duração do passeio
Tempo de percurso
Tempo do percurso até o local do passeio.
Distância do passeio
Limite de carga por passeio ou guia

Comissão paga pelo fornecedor %
Categoria select
Fornecedor select

Observações do passeio
Link para imagens
Exibir os passeio nos sites de vendas

Imagem de destaque para o site .file


Dados para SEO
Title
Description



Vínculo ao sistema BTMS e Voucher Digital
Codigo BTMS
"""
