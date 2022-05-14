from django.db import models
from django.dispatch import receiver
from destiny.models import Destiny
from season.models import Season

from django.db.models.signals import post_save
from django.utils.text import slugify


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
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, related_name='cadpax_passeio')
    cadpax = models.ForeignKey(TripCategoryPax, on_delete=models.DO_NOTHING, related_name='cadpax_passeio')


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

    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, verbose_name='Passeio')
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
def trip_prices(sender, instance, created, **kwargs):

    trip_option = TripOption.objects.last()
    trip = Trip.objects.filter(id=trip_option.trip.id)
    cadpax = TripCadPaxTrip.objects.all()
    season = Season.objects.all()

    # tp = TripPrice.objects.all()
    # tpi = []
    # for tp in tp:
    #     if trip_option.id == tp.trip_option.id:
    #         tpi=tp.trip_option.id

    # try:
    #     if tpi.exists():
    #         print('TripPrice já!')
    # except:
    for a in trip:
        # print(a, ' - ', a.destiny)
        for i in cadpax:
            if i.trip == a:
                # print('    ', i.cadpax)
                for s in season:
                    if s.destiny == a.destiny:
                        # print(s.name)
                        TripPrice.objects.create(trip_option=instance, cadpax=i.cadpax, season=s, price=0.00)
        # print('-'*50)

# post_save.connect(trip_prices, sender=TripOption)


'''
https://docs.djangoproject.com/en/3.2/ref/signals/
_state.db is None



https://django-portuguese.readthedocs.io/en/1.0/ref/models/querysets.html#campos-de-pesquisa
try:
    obj = Person.objects.get(first_name='John', last_name='Lennon')
except Person.DoesNotExist:
    obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
    obj.save()
    
obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
                  defaults={'birthday': date(1940, 10, 9)})
'''


# def trip_prices2():
    
#     trip = Trip.objects.filter(id=1)
#     for i in trip:
#         print(f'ID:', i.id, ' Trip:', i.name)
#     trip_option = TripOption.objects.all()
#     # for t in trip_option:
#     #     print(f'TripOption: ', t.trip.id, t.trip.destiny.id, t.trip.destiny)

# trip_prices2()

'''
if Trip.objects.filter(name=a).exists():
    for a in all:
        if not TripCadPaxTrip.objects.filter(cadpax=i.cadpax).exists():
            TripPrice.objects.create(trip_option=instance, cadpax=i.cadpax, season='Temporada', price=0.00)

  try:
      user = User.objects.get(pk=id)
  except User.DoesNotExist:
      
'''

# def trip_prices(sender, instance, created, **kwargs):
#     if created:
#         cpax = TripCategoryPax.objects.all()
#         season = Season.objects.all()
#         for cp in cpax:
#             for se in season:
#                 TripPrice.objects.create(trip_option=instance, cadpax=cp, season=se, price=0.00)

# post_save.connect(trip_prices, sender=TripOption)


