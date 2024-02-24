from django import forms
from .models import SupportTicket, SupportPicture

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['title', 'description', 'pictures']

class SupportPictureForm(forms.ModelForm):
    class Meta:
        model = SupportPicture
        fields = ['picture']
