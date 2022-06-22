from django import forms
from .models import *
from django.contrib.auth.models import User
from dataclasses import fields
from tinymce.models import HTMLField
from crispy_forms.helper import FormHelper
# Create forms here
class EditProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField (required=False)
    name = forms.CharField (required=False)
    bio = forms.CharField (required=False)
    class Meta:
        model = Profile
        fields = ['prof_pic', 'name', 'bio', 'website', 'phone', 'email']
        def __init__ (self, *args, **kwargs):
            super(EditProfileForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
class PostForm(forms.ModelForm):
    # text = HTMLField()
    class Meta:
        model = Post
        fields = ['title', 'blog']
    def __init__ (self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()