from django.shortcuts import render, redirect
from forms import PostForm

# Create your views here.


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm() # Empty form for GET request

    return render(request, 'blog/post_form.html', {'form': form})