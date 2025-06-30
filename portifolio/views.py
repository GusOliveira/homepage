from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

from blog.models import Blog # Import the Blog model

def home(request):
    projects = Project.objects.all()
    return render(request, 'portifolio/home.html', {'projects':projects})

def new_home(request):
    latest_posts = Blog.objects.order_by('-date')[:5] # Get 5 latest posts
    context = {
        'latest_posts': latest_posts,
        'on_new_home': True  # Add this context variable
    }
    return render(request, 'portifolio/new_home.html', context)
