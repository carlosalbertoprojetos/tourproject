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
def create_trip_cadpax_prices(sender, instance, **kwargs):
    # verifica se a trip_id possui cadpax registrado
    # if TripCadPaxTrip.objects.filter(trip_id=instance.id).exists():
    #     sd=TripCadPaxTrip.objects.filter(trip_id=instance.id).first()
    #     print(f'Há cadpax registrado para a trip {sd.trip_id}')
    # else:
    #     print(f'Não há cadpax registrado para a trip {instance.id}')
    
    # lista e seta as trip_id e cadpax_id da tripcadpaxtrip
    tc = TripCadPaxTrip.objects.all()
    trip_id_tc=[]
    cadpax_id_tc=[]
    for i in tc:
        trip_id_tc.append(i.trip_id)
        cadpax_id_tc.append(i.cadpax_id)
    trip_id_tc=set(trip_id_tc)
    cadpax_id_tc=set(cadpax_id_tc)

    # verifica se a trip_id possui cadpax registrado
    # if TripOption.objects.filter(trip_id=instance.id).exists():
    #     tor=TripOption.objects.filter(trip_id=instance.id).first()
    #     print(f'Há option registrado para a trip {tor.trip_id}')
    # else:
    #     print(f'Não há option registrado para a trip {instance.id}')

    # lista e seta as trip_option_id para cada trip existentes em TripOption
    to = TripOption.objects.all()
    trip_id_to=[]
    trip_op_id_to=[]
    for i in to:
        trip_id_to.append(i.trip_id)
        trip_op_id_to.append(i.id)
    trip_id_to=set(trip_id_to)
    trip_op_id_to=set(trip_op_id_to)
    
    # verifica se o trip_id do trip_cadpax_trip consta em trip_option
    tc_to=[]
    for j in trip_id_to:
        for i in trip_id_tc:
            if j == i:
                tc_to.append(i)
    # print(f'Há trip_option para o(s) trip_id(s): {tc_to}')

    # verifica a(s) trip(s) que não possui(em) trip_option(s)
    if len(trip_id_tc) > len(trip_id_to):
        for j in trip_id_tc:
            if not j in trip_id_to:
                print(f'Não há trip_option para a(s) trip_id(s) {j}')
    tc_to=set(tc_to)

    # verifica quais options não possuem trip_price
    # necessário saber se há cadpax para a trip
    ntc_to=[]
    for i in to:
        if not TripPrice.objects.filter(trip_option_id=i.id):
            ntc_to.append(i.id)

    if TripCadPaxTrip.objects.filter(trip_id=instance.id).first() and TripOption.objects.filter(trip_id=instance.id).first():
        # seleciona todos cadpax da trip
        tc = TripCadPaxTrip.objects.filter(trip_id=instance.id)
        cadpax=[]
        for i in tc:
            cadpax.append(i.cadpax_id)
        cadpax_id_tc=set(cadpax_id_tc)

        option = TripOption.objects.filter(trip_id=instance.id).all()

        # para cada trip_option
        for i in option:
            trip = Trip.objects.filter(id=instance.id) 
            season = Season.objects.all()

            # se não houver preços registrados para a trip_id
            if not TripPrice.objects.filter(trip_option_id=i.id).exists():
                print('NÃO EXISTE PRICE, CRIANDO...')

                for a in trip:
                    for b in option: # para cada option
                        for c in cadpax: # para cada cadpax da trip
                            for d in season: # para cada temporada
                                if d.destiny_id == a.destiny_id:
                                    print(a.id, b.id, c, d.id)
                                    top = TripOption.objects.get(id=b.id)
                                    tca = TripCategoryPax.objects.get(id=c)
                                    sea = Season.objects.get(id=d.id)
                                    form = TripPrice(trip_option=top, cadpax=tca, season=sea, price=0.00)
                                    form.save()

            else:
                if not TripCadPaxTrip.objects.filter(trip_id=instance.id).first():
                    print(f'Não há cadpax para a trip {instance.id}')
                if not TripOption.objects.filter(trip_id=instance.id).first():
                    print(f'Não há option para a trip {instance.id}')

                # verificar quais tripcadpax da trip não estão no tripprice
                a = TripPrice.objects.filter(trip_option_id=i.id)
                top = []
                for i in a:
                    top.append(i.cadpax_id)
                top=set(top)

                # informa quais cadpax da trip precisam ser criadas na tripprice
                criar=[]
                if len(cadpax_id_tc) > len(top):
                    for j in cadpax_id_tc:
                        if not j in top:
                            criar.append(j)

                print(f'CRIANDO PRICE PARA AS SEGUINTES CADPAX: {criar}')
                
                for a in trip: 
                    for b in option: # para cada option
                        for c in criar: # para cada cadpax da trip
                            for d in season: # para cada temporada
                                if d.destiny_id == a.destiny_id:
                                    top = TripOption.objects.get(id=b.id)
                                    tca = TripCategoryPax.objects.get(id=c)
                                    sea = Season.objects.get(id=d.id)
                                    form = TripPrice(trip_option=top, cadpax=tca, season=sea, price=0.00)
                                    form.save()
