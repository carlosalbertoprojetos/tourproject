from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from django.utils.text import slugify


from basics.models import CategoryPax
from company.models import Company
from season.models import Season


class TripCategory(models.Model):
    name = models.CharField('Categoria', max_length=255, unique=True)
    slug = models.SlugField(max_length=250)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


@receiver(post_save, sender=TripCategory)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug or instance.slug != slugify(instance.name):
        instance.slug = slugify(instance.name)
        return instance.save()


class Trip(models.Model):
    
    CHD_CHOICES = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),
        ('14','14'),
        ('15','15'),
        ('16','16'),
    ]
    
    name = models.CharField('Nome', max_length=255,)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(
        'Imagem do produto', upload_to="produtos/%Y", blank=True)
    trip_description = models.TextField('Descrição do passeio', blank=True)
    short_description = models.TextField('Descrição curta', blank=True)
    
    politic = models.CharField('Política de CHD', choices=CHD_CHOICES, max_length=2)
    trip_duration = models.CharField('Duração do passeio (hrs)', max_length=255)
    
    travel_time = models.CharField('Tempo de percurso (hrs)', max_length=255)
    travel_time_untoplace = models.CharField('Tempo de percurso até o local do passeio (hrs)', max_length=255)
    
    ride_distance = models.CharField('Distância do passeio (Km)', max_length=255)
    limit_load = models.CharField('Limite de carga por passeio ou guia (Nº de pessoas)', max_length=255)
    commission = models.DecimalField('Comissão paga pelo fornecedor (%)', max_digits=5, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE, verbose_name='Categoria')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    tour_notes = models.TextField('Notas do passeio', blank=True)
    featured_image = models.FileField('Imagem de destaque para o site', upload_to='files/')
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Passeio"
        verbose_name_plural = "Passeios"

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.imagem.url)
        # view_image.short_description = "Imagem Cadastrada"
        # view_image.allow_tags = True

    def __str__(self):
        return self.name


class TripSeasonPrices(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, verbose_name='Passeio')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    cadpax = models.ForeignKey(CategoryPax, on_delete=models.DO_NOTHING, verbose_name='Cadastro PAX')
    price = models.CharField('Preço', max_length=9)

    def __str__(self):
        return self.trip +' - '+ self.season +' - '+ self.cadpax +' - R$ '+ self.price