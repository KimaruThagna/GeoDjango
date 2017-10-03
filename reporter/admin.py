from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidenceAdmin(LeafletGeoAdmin):
    readonly_fields = ['location']
    class Meta:
        model=Incidence

class CountyAdmin(LeafletGeoAdmin):
    list_display = ['counties','codes','cty_code','dis']

    class Meta:

        model=Counties

admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Counties,CountyAdmin)