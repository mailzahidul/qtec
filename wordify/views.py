from django.shortcuts import render
from blog.models import Post

def home_views(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)