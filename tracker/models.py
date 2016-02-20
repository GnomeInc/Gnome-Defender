from django.db import models
from django.contrib.auth.models import User


class DataSet(models.Model):
    """
    This model represents a single point of data, including the following fields
    :user: associated with this gnome's data
    :gnome: gnome that sent this datum
    :date: date of datum harvest
    :time: time of datum harvest
    :temperature: temp at time of datum harvest
    :humidity: humidity at time of datum harvest
    :light_level: light level at time of harvest
    :soil_moisture: soil moisture level normalized to optimal soil moisture for plants
    :nutrient_level: soild nutrient NPK level at time of datum harvest
    """
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    gnome = models.ForeignKey('Gnome', editable=False, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_level = models.IntegerField()
    soil_moisture = models.IntegerField()
    nutrient_level = models.IntegerField()


class Gnome(models.Model):
    """
    This mod/el represents a specific gnome. It has the following fields
    :gnome_model: specifies the specific gnome model as more are developed
    :name: a name given to the gnome by the user at the time of its activation
    :user: the user account associated with this gnome.
    """
    GNOME_MODELS = (
        ('GD', 'Gnome Defender'),
    )

    gnome_model = models.CharField(max_length=20, choices=GNOME_MODELS)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
