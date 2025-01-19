from django.shortcuts import render, get_object_or_404, redirect
from .models import SupportComment
from customer_portal.models import ServiceRequest as CustomerPortalServiceRequest
# from .models import ServiceRequest as SupportServiceRequest  # Importing the ServiceRequest from customer support backend

from .forms import SupportCommentForm
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)
from django.contrib import messages  

@login_required
def support_dashboard(request):

    service_requests = CustomerPortalServiceRequest.objects.all()
 
    status_filter = request.GET.get('status')
    type_filter = request.GET.get('type')
    if status_filter:
        service_requests = service_requests.filter(status=status_filter)
    if type_filter:
        service_requests = service_requests.filter(request_type=type_filter)
    
    
    return render(request, 'customer_support/dashboard.html', {'service_requests': service_requests})

@login_required
def request_detail(request, request_id):
  
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    comments = service_request.comments.all() if hasattr(service_request, 'comments') else None

    if request.method == 'POST':
        form = SupportCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.service_request = service_request
            comment.support_rep = request.user
            comment.save()
            return redirect('customer_support:request_detail', request_id=request_id)
    else:
        form = SupportCommentForm()

    return render(request, 'customer_support/request_detail.html', {
        'service_request': service_request,
        'comments': comments,
        'form': form,
    })
from customer_portal.models import ServiceRequest
from django.http import HttpResponse
@login_required
def update_request_status(request, service_request_id):
    if request.method != 'POST':
        return HttpResponse("This endpoint only accepts POST requests")
    
    # Get the service request instance by ID
    service_request = get_object_or_404(ServiceRequest, id=service_request_id)
    
    # Get the new status and resolution notes from the form data
    new_status = request.POST.get('status')
    resolution_notes = request.POST.get('resolution_notes')
    
    if not new_status:
        return HttpResponse("Status is required")
        
    # Update the service request status
    try:
        old_status= service_request.status
        service_request.status = new_status
        
        # If status is 'Resolved', capture resolution time
        if new_status == 'Resolved' and service_request.resolved_at is None:
            from django.utils import timezone
            service_request.resolved_at = timezone.now()
            
        service_request.save()
        
        # Create a new SupportComment with the resolution notes if provided
        if resolution_notes:
            SupportComment.objects.create(
                service_request=service_request,
                support_rep=request.user,
                comment=resolution_notes
            )
        messages.success(
            request, 
            f"Request status successfully updated from {old_status} to {new_status}."
            + (" Resolution notes added." if resolution_notes else "")
        )
            
        return redirect('customer_support:request_detail', request_id=service_request_id)
        
    except Exception as e:
        # Log the error and return a bad request response
        print(f"Error updating status: {str(e)}")
        return HttpResponse(f"Error updating status: {str(e)}")

