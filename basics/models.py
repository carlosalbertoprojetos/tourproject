from django.db import models

    
class CategoryPax(models.Model):
    name = models.CharField('Categoria PAX', max_length=255)

    def __str__(self):
        return self.name