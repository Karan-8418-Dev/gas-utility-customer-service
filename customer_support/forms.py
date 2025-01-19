from django import forms
from .models import SupportComment

class SupportCommentForm(forms.ModelForm):
    class Meta:
        model = SupportComment
        fields = ['comment']
