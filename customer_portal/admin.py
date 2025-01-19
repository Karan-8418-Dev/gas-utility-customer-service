# Register your models here.
from django.contrib import admin
from .models import ServiceRequest

admin.site.register(ServiceRequest)
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def manage_requests(request):
    all_requests = ServiceRequest.objects.all()
    return render(request, 'customer_portal/manage_requests.html', {'requests': all_requests})
