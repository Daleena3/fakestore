from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    band=models.CharField(max_length=200)
    specs=models.CharField(max_length=230)
    price=models.PositiveIntegerField()

    def  __str__(self):
       return self.name
