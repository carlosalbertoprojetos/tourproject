from destiny.models import Destiny
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from season.models import Season, Event


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

    name = models.CharField('Nome', max_length=255, default='teste', unique=True)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(
        'Imagem do produto', upload_to="passeio/%Y", blank=True)
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

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class CategoryPax(models.Model):
    name = models.CharField('Nome', max_length=255, unique=True)
    note = models.TextField('Observação', max_length=255, blank=True, null=True)
    t_adult = models.BooleanField('Tarifa de adulto', blank=True, null=True)
    t_child = models.BooleanField('Tarifa de criança', blank=True, null=True)
    t_guest = models.BooleanField('Tarifa de convidado', blank=True, null=True)
    age_min = models.IntegerField('Idade Mínima', blank=True, null=True)
    age_max = models.IntegerField('Idade Máxima', blank=True, null=True)

    class Meta:
        verbose_name = "Categoria PAX de Passeio"
        verbose_name_plural = "Categorias PAX de Passeio"

    def __str__(self):
        return str(self.name)


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

    # trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Passeio', related_name='activities')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Passeio')
    name = models.CharField('Atividade', max_length=255)
    image = models.ImageField(
    'Imagem da atividade', upload_to="atividade/%Y", blank=True)
    description = models.TextField('Descrição da atividade', blank=True)
    catpax = models.ManyToManyField(CategoryPax, verbose_name=('Categoria PAX'), blank=True, through='ActivityCatPax')
    min_amount_pax = models.IntegerField('Quantidade mínima PAX')
    occ_scale = models.CharField('Escala de Ocupação diária (1 a 10)', max_length=2, choices=SCALE_CHOICE)
    tariff_group = models.BooleanField('A tarifa é de Grupo',)
    customer_option = models.BooleanField('A opção pode ser selecionada pelos clientes nos sites?')
    night_walk = models.BooleanField(' O passeio é realizado somente no período noturno?')

    class Meta:
        verbose_name = "Atividade do Passeio"
        verbose_name_plural = "Atividades do Passeio"

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    
""" def get_prices(data_inicio, data_fim):
    
    1- pegar o destino
    2- ter a data inicio e a data fim
    3- pegar os eventos que estao dentro da data inicio e data fim
    4 - se nao tiver nenhum evento retorna o preco da baixa temporada
    5- se tiver eventos(so pode ter um, mas como o codigo nao bloqueia isso pode retornar 2)
    se retornar mais de 1 nao importa, retorna o primeiro evento
    6- pega a temporada do primeiro evento
    7- pega o preco referente a temporada, esta na tabela ActivityPrice

    # import pdb;pdb.set_trace()
    #1
    destino = self.trip.destiny
    #2 
    #3
    #
    # eventos = Events.objects.filter(__range=(start, end))
    #4
    if not eventos:
        prices = self.trip.activityprice
        for o in prices:
            if o.season.baixa:
                return price
    #5
    else:
        if len(eventos) > 1:
            eventos = eventos[0]
            # aqui so pego 2 eventos
    #6 """


class ActivityCatPax(models.Model): 
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE )
    catpax = models.ForeignKey(CategoryPax, on_delete=models.CASCADE )

    def __str__(self):
        return str(self.catpax)


class ActivityPrice(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='')
    catpax = models.ForeignKey(CategoryPax, on_delete=models.CASCADE, verbose_name='Categoria PAX')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='Temporada')
    price = models.DecimalField('',max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Preço da atividade"
        verbose_name_plural = "Preços das atividades"

    def __str__(self):
        return self.activity.name
    

# deleta catpax quando desmarcado(desflegado) da activity por manytomany
@receiver(post_delete, sender=ActivityCatPax)
def delete_trip_catpax_prices(sender, instance, **kwargs):
    tcp = ActivityPrice.objects.filter(catpax_id=instance.catpax_id)    
    to = Activity.objects.filter(id=instance.activity_id)

    for i in tcp:
        for j in to:
            if i.activity_id == j.id:
                ActivityPrice.objects.filter(id=i.id).delete()


# date_arrival, date_departure
#-========================================= TESTES#
def trips_filter(id_destiny, data_inicio, datafim):
    trips = Trip.objects.filter(destiny_id=id_destiny)
    activs = Activity.objects.filter(trip__in=trips)  
    import pdb;pdb.set_trace()
    dir(trips[0])
    trips[0].activitys
    return object
    
    #'retorna todas atividades de trips'
    season = Season.objects.filter(destiny_id=id_destiny)
    price = ActivityPrice.objects.filter(ativitity__in=activ)
    period = Event.objects.filter(season__in=season)
    lista_passeios = []
    for t in trips:
        for a in t.atividades: #activs.filter(passeio=o): # o.activs
            
            #[passeio1,passeio2,passeio3]
            #passeio = {'passeio', passeio, 'atividades':[ativ1, ativ2,ativ3]}
            #{'atividade':atividade, 'precos': precos}
            
            lista_passeios.append({'passeio':o, 'atividades':o.activ})
        
    
    # lista passeios/ lista atividades/ lista preços
    for t in trips:
        print(t.id, t.name, t.destiny)
        for a in activ:
                if t.id == a.trip_id:
                    print('      ', a.id, a.name)
    for s in season:
        if s.destiny_id == id_destiny:
            print(s.id, s.name, s.destiny)
    
    
    for p in period:
        print('\n')
        print(p.name_event ,'-',p.season.name, '-', p.season.destiny)
        print('início', p.date_init, '/ fim', p.date_fin, '\n')
    
        for a in activ:
            if a.trip == p:
                print(a.trip)
                print(a.name)

# trips_filter()