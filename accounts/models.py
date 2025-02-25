# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=False, null=True)
    is_customer = models.BooleanField(default=False)
    is_support_rep = models.BooleanField(default=False)
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=False)

    objects = CustomUserManager()  # Set the custom manager
