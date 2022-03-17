from django.db import models

# Create your models here.

class Transport(models.Model):
    stretch = models.CharField('Trecho', max_length=255, unique=True)
    hits = models.PositiveIntegerField('Acessos')
    is_active = models.BooleanField('Ativar',default=True)
    document = models.FileField('Documento', upload_to='files/')
    description = models.TextField('Descrição', blank=True)
    
    class Meta:
        ordering = ('stretch',)
        verbose_name ='Transporte'
        verbose_name_plural ='Transportes'
    
    def __str__(self):
        return self.stretch