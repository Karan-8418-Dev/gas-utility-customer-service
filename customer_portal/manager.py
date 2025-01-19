from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_support_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a support user with an email and password.
        """
        extra_fields.setdefault('is_support', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_customer_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a customer user with an email and password.
        """
        extra_fields.setdefault('is_customer', True)
        return self.create_user(username, email, password, **extra_fields)
