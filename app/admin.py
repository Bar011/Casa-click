from django.contrib import admin
from .models import Inmueble, SolicitudArriendo, Region,Comuna

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)
admin.site.register(Region)
admin.site.register(Comuna)