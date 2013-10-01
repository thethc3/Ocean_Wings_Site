__author__ = 'thomas'
from django.contrib import admin
from .models import Pilot, Appointment, Aircraft

class PilotsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pilot, PilotsAdmin)


class AppointmentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentsAdmin)


class AircraftAdmin(admin.AdminSite):
    pass
admin.site.register(Aircraft, AppointmentsAdmin)