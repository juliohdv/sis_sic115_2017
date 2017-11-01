from django.db import models

# Create your models here.

class Cuenta(models.Model):
	id = models.AutoField(primary_key=True)
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)
	especificaiones = models.CharField(max_length=200)
	debe = models.FloatField()
	haber = models.FloatField()


