from django.db import models

# Create your models here.

class MPeople(models.Model):

	name = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	country = models.CharField(max_length=50)
	cep = models.CharField(max_length=50)
	phone = models.CharField(max_length=13, blank=True)
	gender = models.CharField(max_length=1)
	email = models.EmailField(blank=True)
	birthday = models.DateField(blank=True)
	cpf = models.CharField(max_length=11)