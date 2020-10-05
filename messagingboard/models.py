from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Messagingboard(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)
    posted_by= models.ForeignKey(get_user_model(), on_delete= models.CASCADE,)

    def __str__(self):
        return self.title





class Comment(models.Model):
    message = models.ForeignKey(Messagingboard, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)
    comment_by= models.ForeignKey(get_user_model(), on_delete= models.CASCADE,)

    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('messagingboard_list')
