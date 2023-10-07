# models.py

from django.db import models

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    # Add other fields as needed for your user profile

    def __str__(self):
        return self.username
