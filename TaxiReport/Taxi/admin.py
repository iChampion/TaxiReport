from django.contrib import admin

# Register your models here.
from Taxi.models import Cars


class CarsAdmin(admin.ModelAdmin):
    list_display = (
        'marka', 'model', 'vincode', 'Agestart', 'ctc', 'number', 'inwork', 'active', 'createown', 'datacreate',
    )

admin.site.register(Cars, CarsAdmin)