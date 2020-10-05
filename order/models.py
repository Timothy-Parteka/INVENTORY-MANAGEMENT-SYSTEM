from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

# Create your models here.

class OrderItem(models.Model):

    PENDING = 'pending'
    ACCEPTED = 'accepted'


    Ordered = (

                ('PENDING', 'pending'),
                ('ACCEPTED', 'accepted'),

    )

    item = models.CharField(max_length=255)
    count = models.CharField(max_length=255, blank=True, null=True)
    date_ordered = models.DateTimeField(default=now)
    reason_for_order = models.TextField()
    ordered_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ordered = models.CharField(max_length=255,choices=Ordered, default=PENDING)

    def __str__(self):
        return self.item
