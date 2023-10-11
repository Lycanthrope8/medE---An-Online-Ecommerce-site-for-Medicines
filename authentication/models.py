# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     phone_number = models.CharField(max_length=15, unique=True)
#     first_name = models.CharField(max_length=255, default='')  # Added first name field
#     last_name = models.CharField(max_length=255, default='')  # Added last name field
#     dob = models.DateField(null=True, blank=True)  # Added Date of Birth field
#     email = models.EmailField(max_length=255, default='')  # Added email field
#     address = models.TextField(default='')  # Added address field



###############################################
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserProfileManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number field must be set')
        extra_fields.setdefault('is_active', True)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(unique=True, max_length=15)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'

    class Meta:
        permissions = [
            ("change_own_userprofile", "Can change own user profile"),
        ]

    def __str__(self):
        return self.phone_number