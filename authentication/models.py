from django.db import models

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number

