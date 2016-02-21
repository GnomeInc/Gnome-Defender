from django.contrib import admin

from .models import DataSet, Gnome


class DataSetAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('date', 'time'), ('temperature', 'humidity', 'light_level', 'soil_moisture', 'nutrient_level'),
                       'gnome', 'user']
        }),
    )
    list_display = ('date', 'time', 'temperature', 'humidity', 'gnome')
    list_filter = ['date']


class GnomeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('name', 'gnome_model', 'user')]
        }),
    )

    list_display = ('name', 'gnome_model', 'user')


admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Gnome, GnomeAdmin)
