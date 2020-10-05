from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

      ################################
# Create model for LAND ADMIN INVENTORY

class FloorLocation(models.Model):

    location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.location


class TenthFloorDataEntryDeskTop(models.Model):
    # IN_CURRENT_LOCATION = 'In Current Location'
    # LAND_REGISTRATION = 'Land Registration'
    # THIRD_FLOOR = 'Third Floor'
    # FOURTH_FLOOR_WING_A = 'Fourth Floor Wing A'
    # SEVENTH_FLOOR = 'Seventh Floor'
    # TENTH_FLOOR_FORMER_PREVALIDATION_ROOM = 'Tenth Floor Former Prevalidation Room'
    # LOCATION = (
    #         (IN_CURRENT_LOCATION, 'In Current Location'),
    #         (LAND_REGISTRATION, 'Land Registration'),
    #         (THIRD_FLOOR, 'Third Floor'),
    #         (FOURTH_FLOOR_WING_A, 'Fourth Floor Wing A'),
    #         (SEVENTH_FLOOR, 'Seventh Floor'),
    #         (TENTH_FLOOR_FORMER_PREVALIDATION_ROOM, 'Tenth Floor Former Prevalidation Room'),
    #     )
    cpu_serial_number = models.CharField(max_length=200)
    monitor_serial_number = models.CharField(max_length=200)
    keyboard_serial_number = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    floor_location = models.ForeignKey(FloorLocation, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.cpu_serial_number

    def get_absolute_url(self):
        return reverse('tenthfloordataentrydesKtopdetails', args=[str(self.id)])
