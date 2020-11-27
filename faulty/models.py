from django.db import models
from django.utils.timezone import now


# Create your models here.

class Faulty(models.Model):
    # NONE = 'None'
    # LAND_ADMIN = 'Land Admin'
    # LAND_REGISTRATION = 'Land Registration'
    # THIRD_FLOOR = 'Third Floor'
    # FOURTH_FLOOR_WING_A = 'Fourth Floor Wing A'
    # FOURTH_FLOOR_WING_B = 'Fourth Floor Wing B'
    # SEVENTH_FLOOR = 'Seventh Floor'
    # TENTH_FLOOR_WING_C = 'Tenth Floor Wing C'
    # TENTH_FLOOR_DATAENTRY = 'Tenth Floor Data Entry'
    # TENTH_FLOOR_FORMER_PREVALIDATION_ROOM = 'Tenth Floor Former Prevalidation Room'
    # LOCATION = (
    #         (NONE, 'None'),
    #         (LAND_ADMIN, 'Land Admin'),
    #         (LAND_REGISTRATION, 'Land Registration'),
    #         (THIRD_FLOOR, 'Third Floor'),
    #         (FOURTH_FLOOR_WING_B, 'Fourth Floor Wing B'),
    #         (SEVENTH_FLOOR, 'Seventh Floor'),
    #         (TENTH_FLOOR_WING_C, 'Tenth Floor Wing C'),
    #         (TENTH_FLOOR_DATAENTRY, 'Tenth Floor Data Entry'),
    #         (TENTH_FLOOR_FORMER_PREVALIDATION_ROOM, 'Tenth Floor Former Prevalidation Room'),
    #     )
    
    ITEM_REPAIRED = (
        ('PENDING', 'pending')
        ('REPAIRED', 'repaired')
    )

    item = models.CharField(max_length=200)

    item_serial_number = models.CharField(max_length=200, unique=True)

    faulty_description = models.TextField()

    from_location = models.CharField(max_length=200)

    repaired = models.CharField(max_length=200, choices=ITEM_REPAIRED, null=True)

    date_repaired = models.DateTimeField(default=now, null=True, blank=True)

    location_returned = models.CharField(max_length=200, null=True, blank=True)




    def __str__(self):
        return self.item_serial_number
