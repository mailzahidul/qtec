from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.qtec_problem_0, name="qtec-search"),
    path('search_data/', views.searched_data, name='searched_data')
]