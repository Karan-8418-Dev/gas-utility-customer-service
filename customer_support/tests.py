from django.test import TestCase

# Create your tests here.
# customer_support/tests.py
from django.test import TestCase
from customer_portal.models import ServiceRequest

class CustomerSupportTest(TestCase):
    def test_update_request_status(self):
        request = ServiceRequest.objects.create(
            customer_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            request_type="Gas Leak",
            description="A description",
            status="Pending",
        )
        request.status = "Resolved"
        request.save()
        self.assertEqual(request.status, "Resolved")
