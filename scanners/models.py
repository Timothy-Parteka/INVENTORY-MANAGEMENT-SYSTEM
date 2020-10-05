from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Scanner(models.Model):
    serial_number = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.serial_number
