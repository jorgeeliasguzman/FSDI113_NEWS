from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import PositiveIntegerField


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)