from django.db import models
from django.utils.translation import gettext_lazy as _


class Destiny(models.Model):

    STATE_CHOICES = [
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO'),
    ]

    name = models.CharField('Destino', max_length=255,)
    state = models.CharField(_('Estado'), choices=STATE_CHOICES, max_length=2)
    city = models.CharField('Cidade',
                            max_length=100,
                            null=True,
                            blank=True,
                            )
    active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.name + ': ' + self.city + '/' + self.state

    STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
    
    )

    name = models.CharField('Destino Turístico', max_length=255,)    
    city = models.CharField('Cidade', max_length=100, null=True)
    state = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Destino Turístico'
        verbose_name_plural = 'Destinos Turísticos'

    def __str__(self):
        return self.name