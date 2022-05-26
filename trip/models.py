from django.db import models
from django.db.models.signals import post_save, post_delete, m2m_changed, post_migrate
from django.dispatch import receiver
from django.utils.text import slugify

from destiny.models import Destiny
from season.models import Season

class TripCategoryPax(models.Model):
    name = models.CharField('Categoria PAX', max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria PAX de Passeio"
        verbose_name_plural = "Categorias PAX de Passeio"


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
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE, verbose_name='Categoria')
    
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    
    cadpax = models.ManyToManyField(TripCategoryPax, verbose_name=('Categoria PAX'), blank=True, related_name='catpax', through='TripCadPaxTrip')
    
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


class TripCadPaxTrip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    cadpax = models.ForeignKey(TripCategoryPax, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['trip','cadpax']]

    def __str__(self):
        return self.cadpax


class TripOption(models.Model):

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
    name = models.CharField('Nome', max_length=255)
    description = models.TextField('Descrição do passeio', blank=True)
    min_amount_pax = models.IntegerField('Quantidade mínima PAX')
    occ_scale = models.CharField('Escala de Ocupação diária (1 a 10)', max_length=2, choices=SCALE_CHOICE)
    tariff_group = models.BooleanField('A tarifa é de Grupo',)
    customer_option = models.BooleanField('A opção pode ser selecionada pelos clientes nos sites?',)
    night_walk = models.BooleanField(' O passeio é realizado somente no período noturno?',)

    def __str__(self):
        return self.name


class TripPrice(models.Model):
    trip_option = models.ForeignKey(TripOption, on_delete=models.CASCADE, verbose_name='')
    cadpax = models.ForeignKey(TripCategoryPax, on_delete=models.CASCADE, verbose_name='Categoria PAX')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='Temporada')
    price = models.DecimalField('',max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        # return self.trip_option +' - '+ self.season +' - '+ self.cadpax +' - R$ '+ self.price
        return self.trip_option


@receiver(post_save, sender=TripOption)
def create_trip_prices(sender, instance, created, **kwargs):
    if created:
        trip_option = TripOption.objects.last()
        trip = Trip.objects.filter(id=trip_option.trip.id)
        cadpax = TripCadPaxTrip.objects.all()
        season = Season.objects.all()

        for a in trip:
            for i in cadpax:
                if i.trip == a:
                    for s in season:
                        if s.destiny == a.destiny:
                            TripPrice.objects.create(trip_option=instance, cadpax=i.cadpax, season=s, price=0.00)
                            

@receiver(post_delete, sender=TripCadPaxTrip)
def delete_trip_cadpax_prices(sender, instance, **kwargs):
    tcp = TripPrice.objects.all()
    tp_id=[]
    for i in tcp:
        if i.cadpax_id == instance.cadpax_id:
            tp_id.append(i.id)
            TripPrice.objects.filter(id=i.id).delete()

@receiver(post_save, sender=Trip)
# @receiver(post_migrate, sender=TripCadPaxTrip)
def create_trip_cadpax_prices(sender, instance, **kwargs):
    tct = TripCadPaxTrip.objects.last()
    tcp = TripPrice.objects.all()
    top = TripOption.objects.all()

    trip=instance.id
    trip_op=[]
    for i in top:
        if i.trip_id == tct.trip_id:
            trip_op = i.id

    if trip_op:
        trip_cad=[]
        season=[]
        price_cad=[]
        new=[]

        # identificar objeto criado
        trip_cadpax = TripCadPaxTrip.objects.all()
        for i in trip_cadpax:
            if i.trip_id == trip:
                trip_cad.append(i.cadpax_id)

        for i in tcp:
            if i.trip_option_id == trip_op:
                season.append(i.season_id)
                price_cad.append(i.cadpax_id)

        season=set(season)
        price_cad=set(price_cad)

        # tem em trip_cap e não tem em price_cad
        for i in trip_cad:
            if not i in price_cad:
                new.append(i)

        # criar preços para cada novo cadpax
        for s in season:
            for t in trip_cad:
                if not t in price_cad:
                    print(f'cadpax: {t} season: {s} t_option: {trip_op}')
                    top = TripOption.objects.get(id=trip_op)
                    tca = TripCategoryPax.objects.get(id=t)
                    sea = Season.objects.get(id=s)
                    form = TripPrice(trip_option=top, cadpax=tca, season=sea, price=0.00) 
                    form.save()

# o que tem em cadpaxtrip e não tem em tripprice
