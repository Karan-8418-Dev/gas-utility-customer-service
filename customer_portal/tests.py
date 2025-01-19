from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import ServiceRequest

class ServiceRequestTest(TestCase):
    def test_service_request_creation(self):
        request = ServiceRequest.objects.create(
            customer_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            request_type="Gas Leak",
            description="A description",
        )
        self.assertEqual(request.customer_name, "John Doe")
