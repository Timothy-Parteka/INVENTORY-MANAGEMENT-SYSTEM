from django.contrib import admin
from .models import LandAdminDeskTop, LandAdminBarCodeScanner, FloorLocation

# Register your models here.

admin.site.register(LandAdminDeskTop)
admin.site.register(LandAdminBarCodeScanner)
admin.site.register(FloorLocation)
