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
    name = models.CharField('Atividade', max_length=255)
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
    tcp = TripPrice.objects.filter(cadpax_id=instance.cadpax_id)    
    to = TripOption.objects.filter(trip_id=instance.trip_id)

    for i in tcp:
        for j in to:
            if i.trip_option_id == j.id:
                # print(f'TO {i.trip_option_id}, CA {i.cadpax_id}, ID {i.id}')
                TripPrice.objects.filter(id=i.id).delete()


@receiver(m2m_changed, sender=Trip.cadpax.through)
@receiver(post_save, sender=Trip)
def create_trip_cadpax_prices(sender, instance, **kwargs):
    # Seleciona a trip
    trip = Trip.objects.filter(id=instance.id)
    # Verifica se há activity (trip-option) para a trip   
    options = TripOption.objects.filter(trip_id=instance.id).first()
    # Seleciona os registros de preço por activity (trip_option)
    price = TripPrice.objects.filter(trip_option_id=options)
    # Seleciona as cadpax registradas por trip
    cadpax = TripCadPaxTrip.objects.filter(trip_id=instance.id)
    # Seleciona as activities (trip_options) por trip
    to_all = TripOption.objects.filter(trip_id=instance.id)
    season = Season.objects.all()

    # Se não existir registro de preços para a trip
    if not price:
        # se houver cadpax e activity (tripOption) para a trip, criar tabela de preços
        if cadpax and options:
            for a in trip:
                for b in to_all:
                    for c in cadpax:
                        if c.trip == a:
                            for d in season:
                                if d.destiny == a.destiny:
                                    # print(f'TO {b.id} , CA {c.cadpax_id}, TE {d.id}')
                                    top = TripOption.objects.get(id=b.id)
                                    tca = TripCategoryPax.objects.get(id=c.cadpax_id)
                                    sea = Season.objects.get(id=d.id)
                                    form = TripPrice(trip_option=top, cadpax=tca, season=sea, price=0.00)
                                    form.save()

    # Se existir registro de preços para a trip
    else: 
        # Seleciona todos os cadpax da trip
        cpt=[]
        for i in cadpax:
            cpt.append(i.cadpax_id)
        cpt=set(cpt)

        # Seleciona todos as activities (trip_options) por trip
        to = TripOption.objects.all()
        tot=[]
        for i in to:
            if i.trip_id == instance.id:
                tot.append(i.id)
        tot=set(tot)

        # Seleciona as cadpax da trip_price por trip_option
        tp = TripPrice.objects.all()
        tcp=[]
        for j in tp:
            for i in tot:
                if j.trip_option_id == i:
                    tcp.append(j.cadpax_id)
        tcp=set(tcp)

        # Seleciona os cadpaxes da trip_cadpax_trip que não estão na trip_price (devem ser criados)
        criar=[]
        for i in cpt:
            if not i in tcp:
                criar.append(i)

        if criar:
            for a in trip:
                for b in tot: # para cada option
                    for c in criar: # para cada cadpax da trip
                        for d in season: # para cada temporada
                            if d.destiny_id == a.destiny_id:
                                # print(f'TO {b.id}, CA {c}, TE {d.id}')
                                top = TripOption.objects.get(id=b)
                                tca = TripCategoryPax.objects.get(id=c)
                                sea = Season.objects.get(id=d.id)
                                form = TripPrice(trip_option=top, cadpax=tca, season=sea, price=0.00)
                                form.save()

