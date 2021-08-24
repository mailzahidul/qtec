from django.shortcuts import render
from .forms import SearchForm
from blog.models import Post
from .models import QtechKeywordSearch
from django.contrib import messages
from django.db.models import Count
import datetime
from django.db.models import Q
# Create your views here.


def qtec_problem_0(request):
    if request.method == 'GET':
        forms = SearchForm()
    else:
        forms = SearchForm(request.POST)
        u = "Anonymous user"
        if request.user:
            u = request.user
        if forms.is_valid():
            search_word = forms.cleaned_data['search_keyword']
            date_time=datetime.datetime.now()
            QtechKeywordSearch.objects.create(
                user=u,
                search_keyword=search_word,
                search_time = date_time
            )
            post_obj = Post.objects.filter(
                Q(title__icontains=search_word)|
                Q(body__icontains=search_word)|
                Q(user__username__icontains=search_word)
                )
            context = {
                'forms': forms,
                'posts': post_obj,
                'username': u
            }
            return render(request, 'qtec/search.html', context)


    context = {
        'forms': forms,
    }
    return render(request, 'qtec/search.html', context)


def searched_data(request):
    objs = QtechKeywordSearch.objects.values('search_keyword').annotate(name_count=Count('search_keyword')).filter(name_count__gt=0)
    context = {
        'objs': objs
    }
    return render(request, 'qtec/searched_data.html', context)
