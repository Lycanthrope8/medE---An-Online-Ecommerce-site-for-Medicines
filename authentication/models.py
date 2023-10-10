from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=255, default='')  # Added first name field
    last_name = models.CharField(max_length=255, default='')  # Added last name field
    dob = models.DateField(null=True, blank=True)  # Added Date of Birth field
    email = models.EmailField(max_length=255, default='')  # Added email field
    address = models.TextField(default='')  # Added address field

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # other fields if any ...

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'

    # Unique related name to avoid clashes with auth.User model
    groups = models.ManyToManyField('auth.Group', related_name='user_profiles', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_profiles', blank=True)

    # other fields if any ...
