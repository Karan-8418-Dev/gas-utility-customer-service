from django import forms
from .models import ServiceRequest
from accounts.models import CustomUser

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name','address', 'email', 'phone_number', 'request_type', 'description', 'file_attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        request_type = forms.ChoiceField(choices=ServiceRequest.REQUEST_TYPE_CHOICES, widget=forms.RadioSelect)
    # Optional: If you want to keep track of the user explicitly in the form
    # user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    def save(self, commit=True):
        # Ensure the user is set automatically when saving the form
        service_request = super().save(commit=False)
        if commit:
            service_request.user = self.instance.user  # Automatically set the user
            service_request.save()
        return service_request


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'address', 'phone_number']  