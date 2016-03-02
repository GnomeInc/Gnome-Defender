from django.contrib import admin

from .models import DataSet, Gnome, GnomeModel, GnomeFeature, Device


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


class GnomeModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('name',), 'features', ]
        }),
    )

    list_display = ('name',)


class GnomeFeatureAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('name',), ]
        }),
    )

    list_display = ('name',)


class DeviceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('device_id', 'device_type', 'user'), ]
        }),
    )

    list_display = ('device_id', 'user')


admin.site.register(GnomeFeature, GnomeFeatureAdmin)
admin.site.register(GnomeModel, GnomeModelAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Gnome, GnomeAdmin)
admin.site.register(Device, DeviceAdmin)
