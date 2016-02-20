from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DataSet(models.Model):
    user = models.ForeignKey('User', editable=False, on_delete=models.CASCADE)
    gnome = models.ForeignKey('Gnome', editable=False, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_level = models.IntegerField()
    soil_moisture = models.IntegerField()


class Gnome(models.Model):
    gnome_model = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    user = models.ForeignKey('User', editable=False, on_delete=models.CASCADE)
