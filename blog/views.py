from django.shortcuts import render
from .models import Post
# Create your views here.


def post_view(request, id):
    post = Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request, 'post-view.html', context)