
from django.db import models
from django.conf import settings

class SupportComment(models.Model):
    service_request = models.ForeignKey(
        'customer_portal.ServiceRequest', on_delete=models.CASCADE, related_name='comments'
    )
    support_rep = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='support_comments'
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on Request #{self.service_request.id} by {self.support_rep}"
