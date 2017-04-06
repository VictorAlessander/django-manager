from django.db import models

# Create your models here.

class MPeople(models.Model):

	name = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=12, blank=True)
	gender = models.CharField(max_length=1)
	email = models.EmailField(blank=True)
	birthday = models.DateField(blank=True)
	cpf = models.CharField(max_length=11)