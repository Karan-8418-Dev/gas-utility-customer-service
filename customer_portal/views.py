from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Import this for authentication
from django.http import HttpResponse
from .models import ServiceRequest
from .forms import ServiceRequestForm
from .forms import ProfileForm

@login_required  # Ensures that only logged-in users can access this view
def service_request_form(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the current user to the service request
            service_request = form.save(commit=False)
            service_request.user = request.user  # Assuming the ServiceRequest model has a 'user' field
            service_request.save()
            return redirect('customer_portal:service_request_success')  # Redirect to a success page
    else:
        form = ServiceRequestForm()

    return render(request, 'customer_portal/service_request_form.html', {'form': form})

@login_required  # Ensures that only logged-in users can access this view
def service_request_success(request):
    return render(request, 'customer_portal/service_request_success.html')

@login_required  # Ensures that only logged-in users can access this view
def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, user=request.user)
    # Make sure the logged-in user can only view their own requests
    return render(request, 'customer_portal/track_request.html', {'service_request': service_request})

# customer_portal/views.py


@login_required
def edit_profile(request):
    # Fetch the logged-in user
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('customer_portal:profile') # Redirect to profile page after saving changes
    else:
        form = ProfileForm(instance=user)

    return render(request, 'customer_portal/edit_profile.html', {'form': form})

# customer_portal/views.py

@login_required
def view_profile(request):
    return render(request, 'customer_portal/view_profile.html', {'user': request.user})

# from django.shortcuts import render

def homepage(request):
    return render(request, 'customer_portal/Homepage.html')

def service_history(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customer_portal/service_history.html', {'service_requests': service_requests})
