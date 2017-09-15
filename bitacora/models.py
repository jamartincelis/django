from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	numero  = models.CharField(max_length=11)
	status = models.CharField(max_length=8)

class Servidores(models.Model):
	nombre = models.CharField(max_length=50)
	ip = models.CharField(max_length=50)
	puerto  = models.CharField(max_length=11)
	servicio = models.CharField(max_length=8)	
	cliente = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	status = models.CharField(max_length=8)