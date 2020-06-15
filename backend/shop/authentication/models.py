from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)