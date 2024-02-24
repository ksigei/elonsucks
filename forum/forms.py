from django import forms
from .models import ForumPost, ForumPicture

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'pictures']

class ForumPictureForm(forms.ModelForm):
    class Meta:
        model = ForumPicture
        fields = ['picture']
