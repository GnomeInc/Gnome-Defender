"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Defender

    Copyright: GnomeInc, Some Rights Reserved
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class DataSet(models.Model):
    """
    This model represents a single point of data, including the following fields
    :user:              associated with this gnome's data
    :gnome:             gnome that sent this datum
    :date:              date of datum harvest
    :time:              time of datum harvest
    :temperature:       temp at time of datum harvest
    :humidity:          humidity at time of datum harvest
    :light_level:       light level at time of harvest
    :soil_moisture:     soil moisture level normalized to optimal soil moisture for plants
    :nutrient_level:    soild nutrient NPK level at time of datum harvest
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='datasets')
    gnome = models.ForeignKey('Gnome', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_level = models.IntegerField()
    soil_moisture = models.IntegerField()
    nutrient_level = models.IntegerField()

    def was_harvested_today(self):
        return self.date == timezone.now().date()

    def __str__(self):
        return self.date.strftime('%m/%d/%y') + " at " + self.time.strftime('%H:%M')


class Gnome(models.Model):
    """
    This mod/el represents a specific gnome. It has the following fields
    :gnome_model:   specifies the specific gnome model as more are developed
    :name:          a name given to the gnome by the user at the time of its activation
    :user:          the user account associated with this gnome.
    """
    GNOME_MODELS = (
        ('GD', 'Gnome Defender'),
    )
    gnome_model = models.CharField(max_length=20, choices=GNOME_MODELS)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gnomes')

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    If user has a token, send it along.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)
