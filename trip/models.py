from django.db import models
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from django.utils.text import slugify

from destiny.models import Destiny
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
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE, verbose_name='Categoria')
    
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name='Destino')
    
    # catpax = models.ManyToManyField(TripCategoryPax, verbose_name=('Categoria PAX'), blank=True, related_name='catpax', through='TripCadPaxTrip')
    
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
    catpax = models.ForeignKey(CategoryPax, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = [['Activity','catpax']]

    def __str__(self):
        return str(self.catpax)


class ActivityPrice(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='')
    catpax = models.ForeignKey(CategoryPax, on_delete=models.CASCADE, verbose_name='Categoria PAX')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='Temporada')
    price = models.DecimalField('',max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.activity

# @receiver(m2m_changed, sender=Activity.catpax.through)
# @receiver(post_save, sender=Activity)
# def create_trip_prices(sender, instance, created, **kwargs):
#     if created:
#         trip=Trip.objects.filter(id=instance.trip_id)
#         activity=Activity.objects.filter(id=instance.id)
#         catpax= ActivityCatPax.objects.all()
#         season=Season.objects.all()
  
#         for t in trip:
#             print('TRIP', t.id)
#             for a in activity:
#                 print(f'  ATIVIDADE {a.id}')
#                 for c in catpax:
#                     if c.activity_id == instance.id:
#                         print(f'    CATPAX {c.id}')
#                         for s in season:
#                             if t.destiny_id == s.destiny_id:
#                                 print(f'      SEASON {s.id}')
                                # ActivityPrice.objects.create(activity=instance, catpax=c.id, season=s.id, price=0.00) 


"""
@receiver(post_delete, sender=ActivityCatPax)
def delete_trip_catpax_prices(sender, instance, **kwargs):
    tcp = ActivityPrice.objects.filter(catpax_id=instance.catpax_id)    
    to = Activity.objects.filter(trip_id=instance.trip_id)

    for i in tcp:
        for j in to:
            if i.activity_id == j.id:
                ActivityPrice.objects.filter(id=i.id).delete()

"""
""" 
@receiver(m2m_changed, sender=Activity.catpax.through)
@receiver(post_save, sender=Activity)
def create_trip_catpax_prices(sender, instance, **kwargs):
    # Seleciona a trip
    trip = Trip.objects.filter(id=instance.id)
    # Verifica se há activity para a trip   
    activities = Activity.objects.filter(trip_id=instance.id).first()
    # Seleciona os registros de preço por activity
    price = ActivityPrice.objects.filter(activity_id=activities)
    # Seleciona as catpax registradas por trip
    catpax = ActivityCatPax.objects.filter(trip_id=instance.id)
    # Seleciona as activities por trip
    to_all = Activity.objects.filter(trip_id=instance.id)
    season = Season.objects.all()

    # Se não existir registro de preços para a trip
    if not price:
        # se houver catpax e activity para a trip, criar tabela de preços
        if catpax and activities:
            for a in trip:
                for b in to_all:
                    for c in catpax:
                        if c.trip == a:
                            for d in season:
                                if d.destiny == a.destiny:
                                    # print(f'TO {b.id} , CA {c.catpax_id}, TE {d.id}')
                                    top = Activity.objects.get(id=b.id)
                                    tca = CategoryPax.objects.get(id=c.catpax_id)
                                    sea = Season.objects.get(id=d.id)
                                    form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                                    form.save()

    # Se existir registro de preços para a trip
    else: 
        # Seleciona todos os catpax da trip
        cpt=[]
        for i in catpax:
            cpt.append(i.catpax_id)
        cpt=set(cpt)

        # Seleciona todos as activities por trip
        to = Activity.objects.all()
        tot=[]
        for i in to:
            if i.trip_id == instance.id:
                tot.append(i.id)
        tot=set(tot)

        # Seleciona as catpax da trip_price por activity
        tp = ActivityPrice.objects.all()
        tcp=[]
        for j in tp:
            for i in tot:
                if j.activity_id == i:
                    tcp.append(j.catpax_id)
        tcp=set(tcp)

        # Seleciona os catpaxes da trip_catpax_trip que não estão na trip_price (devem ser criados)
        criar=[]
        for i in cpt:
            if not i in tcp:
                criar.append(i)

        if criar:
            for a in trip:
                for b in tot: # para cada activity
                    for c in criar: # para cada catpax da trip
                        for d in season: # para cada temporada
                            if d.destiny_id == a.destiny_id:
                                # print(f'TO {b.id}, CA {c}, TE {d.id}')
                                top = Activity.objects.get(id=b)
                                tca = CategoryPax.objects.get(id=c)
                                sea = Season.objects.get(id=d.id)
                                form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                                form.save()

 """

def teste(id):
    # filtro atividades por trip
    trip=Trip.objects.filter(id=id)    
    activity=Activity.objects.all()
    catpax=ActivityCatPax.objects.all()
    season=Season.objects.all()

    # se há atividade para a trip e individualiza cada catpax da atividade
    for t in trip:
        print('TRIP', t.id)
        for a in activity:
            print(f'  ATIVIDADE {a.id}')
            for c in catpax:
                if a.id == c.activity_id:
                    print(f'    CATPAX {c.id}')
                    for s in season:
                        if t.destiny_id == s.destiny_id:
                            print(f'      SEASON {s.id}')

        # for a in activity:
        #     # tp = ActivityPrice.objects.filter(activity_id=activity.id)
        #     for i in tp:
        #         if i.activity_id == id:
        #             catpax.append(i.catpax)
        #             season.append(i.season)

        # catpax=list(set(catpax))
        # season=list(set(season))
        
        # print('CATPAX2', catpax)
        # print(season)
        
# teste(1)