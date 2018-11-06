import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
	#TODO: dodać obsługę wielu imion
	first_name = models.CharField(max_length=200)
	#TODO: dodać obsługę nazwisk I voto i II voto
	last_name = models.CharField(max_length=200)
	
	birth_date = models.DateTimeField('data urodzenia')
	death_date = models.DateTimeField('data śmierci')
	
	def __str__(self):
		return self.first_name + " " + self.last_name;
		
	def is_alive(self):
		return self.death_date < timezone.now()
		
	def get_age(self):
		return timezone.now() - self.birth_date