from django.shortcuts import render, redirect, get_list_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

# Create

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm

    return render(request, 'blog/post_form.html', {'form': form})