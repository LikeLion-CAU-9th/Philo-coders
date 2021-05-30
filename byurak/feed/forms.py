from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "body", "date_time"]
