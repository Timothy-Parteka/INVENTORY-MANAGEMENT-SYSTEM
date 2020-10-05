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


class EighthFloorDeskTop(models.Model):
    # IN_CURRENT_LOCATION = 'In Current Location'
    # LAND_REGISTRATION = 'Land Registration'
    # THIRD_FLOOR = 'Third Floor'
    # FOURTH_FLOOR_WING_A = 'Fourth Floor Wing A'
    # FOURTH_FLOOR_WING_B = 'Fourth Floor Wing B'
    # SEVENTH_FLOOR = 'Seventh Floor'
    # TENTH_FLOOR_WING_C = 'Tenth Floor Wing C'
    # TENTH_FLOOR_DATAENTRY = 'Tenth Floor Data Entry'
    # TENTH_FLOOR_FORMER_PREVALIDATION_ROOM = 'Tenth Floor Former Prevalidation Room'
    # GROUND_FLOOR = 'Ground Floor'
    # LOCATION = (
    #         (IN_CURRENT_LOCATION, 'In Current Location'),
    #         (LAND_REGISTRATION, 'Land Registration'),
    #         (THIRD_FLOOR, 'Third Floor'),
    #         (FOURTH_FLOOR_WING_B, 'Fourth Floor Wing B'),
    #         (SEVENTH_FLOOR, 'Seventh Floor'),
    #         (TENTH_FLOOR_WING_C, 'Tenth Floor Wing C'),
    #         (TENTH_FLOOR_DATAENTRY, 'Tenth Floor Data Entry'),
    #         (TENTH_FLOOR_FORMER_PREVALIDATION_ROOM, 'Tenth Floor Former Prevalidation Room'),
    #         (GROUND_FLOOR, 'Ground Floor'),
    #     )
    cpu_serial_number = models.CharField(max_length=200,unique=True)
    monitor_serial_number = models.CharField(max_length=200, unique=True)
    keyboard_serial_number = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    floor_location = models.ForeignKey(FloorLocation, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.cpu_serial_number

    def get_absolute_url(self):
        return reverse('eighthfloordesktopdetail', args=[str(self.id)])
