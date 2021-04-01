from django.db import models

# Create your models here.

class Enterprise(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 60,blank=False)
    nit = models.BigIntegerField(blank = True)
    gln = models.IntegerField(blank = False)

class Code(models.Model):
    id = models.IntegerField(primary_key = True)
    owner = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    name = models.CharField(max_length = 60, unique=True,blank=False)
    description = models.CharField(max_length = 60,blank = True)