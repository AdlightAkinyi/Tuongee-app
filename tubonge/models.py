from django.db import models

# Create your models here.
import re
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt
from tinymce.models import HTMLField
from django.forms import EmailField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField (max_length=255, blank=True)
    prof_pic = CloudinaryField (blank=True)
    bio = models.CharField (max_length=100)
    website = models.URLField (blank=True, max_length=50)
    phone = PhoneNumberField (blank=True)
    email = models.CharField (max_length=50, blank=True)
    created_on = models.DateTimeField (auto_now_add=True)
    def __str__(self):
        return self.name
    def save_profile(self):
        '''
        Add Profile to database
        '''
        self.save()
class Post (models.Model):
    user = models.ForeignKey (User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=False)
    blog = models.TextField(max_length=255,blank=False)
    posted_on = models.DateTimeField (auto_now_add=True)
    def __str__(self):
        return self.blog

    # def create_post(self):
    #     '''
    #     A method that creates a post
    #     '''
    #     self.save()

    def save_post(self):
        '''add new post'''
        self.save()

    def delete_post(self):
        '''
        A method that deletes a post
        '''
        self.delete()