from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts ordered by creation date
    return render(request, 'blog/home.html', {'posts': posts})  # Render the home template with posts context