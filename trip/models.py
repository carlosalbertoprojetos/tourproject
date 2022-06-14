from destiny.models import Destiny
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from season.models import Season


class TripCategory(models.Model):
    name = models.CharField('Categoria', max_length=255, unique=True)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


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
    
    name = models.CharField('Nome', max_length=255, default='teste')
    slug = models.SlugField(max_length=250)
    image = models.ImageField(
        'Imagem do produto', upload_to="produtos/%Y", blank=True)
    trip_description = models.TextField('Descrição do passeio', blank=True, default='teste')
    short_description = models.TextField('Descrição curta', blank=True, default='teste')
    
    politic = models.CharField('Política de CHD', choices=CHD_CHOICES, max_length=2)
    trip_duration = models.CharField('Duração do passeio (hrs)', max_length=255, default='1')
    
    travel_time = models.CharField('Tempo de percurso (hrs)', max_length=255, default='00:00')
    travel_time_untoplace = models.CharField('Tempo de percurso até o local do passeio (hrs)', max_length=255, default='00:00')
    
    ride_distance = models.CharField('Distância do passeio (Km)', max_length=255, default='1')
    limit_load = models.CharField('Limite de carga por passeio ou guia (Nº de pessoas)', max_length=255, default='6')
    commission = models.DecimalField('Comissão paga pelo fornecedor (%)', max_digits=5, decimal_places=2, blank=True, null=True, default='10')
    category = models.ForeignKey(TripCategory, on_delete=models.DO_NOTHING, verbose_name='Categoria')
    
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    
    tour_notes = models.TextField('Notas do passeio', blank=True, default='teste')
    featured_image = models.FileField('Imagem de destaque para o site', upload_to='files/')
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Passeio"
        verbose_name_plural = "Passeios"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CategoryPax(models.Model):
    name = models.CharField('Categoria PAX', max_length=255)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Categoria PAX de Passeio"
        verbose_name_plural = "Categorias PAX de Passeio"


class Activity(models.Model):

    SCALE_CHOICE = [
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
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Passeio')
    name = models.CharField('Atividade', max_length=255)
    description = models.TextField('Descrição do passeio', blank=True)
    catpax = models.ManyToManyField(CategoryPax, verbose_name=('Categoria PAX'), blank=True, through='ActivityCatPax')
    min_amount_pax = models.IntegerField('Quantidade mínima PAX')
    occ_scale = models.CharField('Escala de Ocupação diária (1 a 10)', max_length=2, choices=SCALE_CHOICE)
    tariff_group = models.BooleanField('A tarifa é de Grupo',)
    customer_option = models.BooleanField('A opção pode ser selecionada pelos clientes nos sites?')
    night_walk = models.BooleanField(' O passeio é realizado somente no período noturno?')

    def __str__(self):
        return self.name


class ActivityCatPax(models.Model): 
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    catpax = models.ForeignKey(CategoryPax, on_delete=models.DO_NOTHING)

    # class Meta:
    #     unique_together = [['Activity','catpax']]

    def __str__(self):
        return str(self.catpax)


class ActivityPrice(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='')
    catpax = models.ForeignKey(CategoryPax, on_delete=models.DO_NOTHING, verbose_name='Categoria PAX')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    price = models.DecimalField('',max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.activity


# deleta catpax excluído(desflegado) da activity por manytomany
@receiver(post_delete, sender=ActivityCatPax)
def delete_trip_catpax_prices(sender, instance, **kwargs):
    tcp = ActivityPrice.objects.filter(catpax_id=instance.catpax_id)    
    to = Activity.objects.filter(id=instance.activity_id)

    for i in tcp:
        for j in to:
            if i.activity_id == j.id:
                ActivityPrice.objects.filter(id=i.id).delete()
