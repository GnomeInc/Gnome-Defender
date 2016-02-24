from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DataSet, Gnome


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = (
            'id', 'gnome', 'date', 'time', 'temperature', 'humidity', 'light_level', 'soil_moisture', 'nutrient_level'
        )


class GnomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gnome
        fields = (
            'id', 'gnome_model', 'name', 'user'
        )


class UserSerializer(serializers.ModelSerializer):
    gnomes = serializers.PrimaryKeyRelatedField(many=True, queryset=Gnome.objects.all())

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'gnomes'
        )
