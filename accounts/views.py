from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegistrationForm
# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('customer_portal:service_request_form')  # Redirect to the service request page

            if user.is_support_rep:
                return redirect('customer_support:dashboard')  # Redirect to the support dashboard
            elif user.is_customer:
                # return redirect('customer_portal:homepage')  # Redirect to the customer homepage
                return redirect('customer_portal:homepage')
            else:
                return redirect('accounts:login')  # Default fallback
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # Redirect to the login page

# Register View (Sign-Up)
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()

            # Assign the selected role from the form
            role = request.POST.get('role')
            if role == 'support':
                user.is_support_rep = True
            else:
                user.is_customer = True  # Default to customer

            user.save()
            return redirect('accounts:login')   # Redirect to the login page after successful registration
    else:
                form = RegistrationForm()  # Instantiate the form here
    return render(request, 'accounts/register.html', {'form': form})
