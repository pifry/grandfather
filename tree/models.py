from django.db import models

# Create your models here.

class Person(models.Model):
	#TODO: dodać obsługę wielu imion
	first_name = models.CharField(max_length=200)
	#TODO: dodać obsługę nazwisk I voto i II voto
	last_name = models.CharField(max_length=200)
	
	birth_date = models.DateTimeField('data urodzenia')
	death_date = models.DateTimeField('data śmierci')