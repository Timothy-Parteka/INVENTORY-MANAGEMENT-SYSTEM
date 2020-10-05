from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.
class Department(models.Model):

    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department


class Role(models.Model):

    role = models.CharField(max_length=255)


    def __str__(self):
        return self.role


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    id_number = models.CharField(max_length=255,unique=True,null=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
