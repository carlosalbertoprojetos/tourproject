from django.db import models

# Create your models here.


class Client(models.Model):	
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=254,unique=True)
	cel = models.CharField(max_length=15)
	is_active = models.BooleanField(default=True)

	