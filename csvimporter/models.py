from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=30)
	email =  models.EmailField(blank=True)
	birth_date = models.DateField()
	location = models.CharField(max_length=100, blank=True)
	

class Upload(models.Model):
	file = models.FileField(upload_to='csv', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


class PartnerAuxiliar(models.Model):
    nombre = models.CharField( max_length=80)
    fan_dun = models.CharField( max_length=80)
    grupo_especial = models.BooleanField()
    activo =  models.BooleanField()

    def __unicode__(self):
        return self.nombre

    
