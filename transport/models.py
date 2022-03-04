from django.db import models


# Create your models here.


class Transport(models.Model):   
    trecho = models.CharField(max_length=200)
    acessos = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    
    