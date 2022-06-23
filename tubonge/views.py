from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nav(request):
    return render(request , 'navbar.html')
def about(request):
    return render(request,'about.html')
def footer(request):
    return render(request,'footer.html')
def contact(request):
    return render(request,'contact.html')
def dashboard(request):
    
    return render(request, 'dashboard.html')


def homepage(request):
    # all_posts = Post.objects.all().order_by('id').reverse()
    # context={
    #     'all_posts':all_posts
    # }
    all_posts=Post.objects.all()
    return render(request,'homepage.html',{"all_posts":all_posts})

# User's Profile
@login_required (login_url='/accounts/login/')
def profile(request,id):
    user_profile = Profile.objects.get(id = id)
    user_posts = Post.objects.filter(owner=id)
    context={
        'user_profile': user_profile,
        'user_posts': user_posts
    }
    return render(request, 'profile.html', context=context)
# Updating User's Profile
@login_required (login_url='/accounts/login/')
def profile_update(request, username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)
    data = get_object_or_404 (Profile, id=user_profile.id)
    profile_form = EditProfileForm(instance=data)
    if request.method == 'POST':
        profile_form = EditProfileForm (request.POST, request.FILES, instance=data)
        if profile_form.is_valid():
            profile_form.save()
            return redirect ('profile_update', username=user_name)
        else:
            profile_form = EditProfileForm()
    context={
         'user_name':user_name,
         'profile_form':profile_form,
         'user_profile':user_profile
     }
    return render(request, 'profile_update.html', context=context)
# Creating a New Post
@login_required(login_url='/accounts/login/')
def create_post(request ):
    user = request.user
    post_form= PostForm(request.POST, request.FILES)  
    if request.method == "POST":
       
        if post_form.is_valid():
            # user = request.user
            # title = post_form.cleaned_data.get('title')
            # blog = post_form.cleaned_data.get('blog')
            # user = Profile.objects.get(user=user.id)
            # new_post = Post(
                
            #     title=title,
            #     blog=blog,
            # )
            # post_form.save() 
            post=post_form.save(commit=False)
            post.user=request.user
            post.save
            return redirect('homepage')
        else:
            post=PostForm()
    return render(request,'create_post.html', {'post_form':post_form})
# Viewing the posts
@login_required(login_url='login')
def post_details(request,id):
    post = Post.objects.get(id=id)
    user = Profile.objects.get(id=post.owner.id)
    context={
        'post':post,
        'user':user
    }
    return render(request,'post_details.html',context=context)






