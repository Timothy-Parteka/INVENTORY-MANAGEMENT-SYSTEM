from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class StockIn(models.Model):
    
    ITEM_RECEIVED = (

    ('YES', 'yes'),
    ('NO', 'no'),

    )
    item = models.CharField(max_length=100)
    item_ref_no = models.CharField(max_length=255,null=True, blank=True)
    count = models.CharField(max_length=100)
    date_purchased = models.DateTimeField(default=now)
    business_name = models.CharField(max_length=255, null=True, blank=True)
    item_received = models.CharField(max_length=255, choices=ITEM_RECEIVED, null=True, verbose_name='item received')
    date_received = models.DateTimeField(default=now)
    received_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.item_ref_no
