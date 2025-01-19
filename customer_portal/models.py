from django.db import models
from django.contrib.auth.models import AbstractUser  # Your custom user model
from django.conf import settings  # To reference the custom user model

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    REQUEST_TYPE_CHOICES = [
        ('Billing', 'Billing Issues'),
        ('Outage', 'Service Outage'),
        ('Other', 'Other')
    ]
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()
    file_attachment = models.ImageField(upload_to='complaints/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date=models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    # Adding a relationship to the User model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1,related_name='portal_service_requests')

    def __str__(self):
        return f"{self.customer_name} - {self.request_type} - {self.status}"
