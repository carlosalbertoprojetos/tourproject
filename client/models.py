from django.db import models

# Create your models here.


class Client(models.Model):
	name = models.CharField(primary_key=True,max_length=6)
	email = models.EmailField(max_length=254,unique=True)
	cel = models.CharField(max_length=15)

	def __str__(self):
		return self.nome