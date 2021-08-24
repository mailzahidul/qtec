from django.urls import path
from . import views

urlpatterns = [
    path('post-view/<int:id>', views.post_view, name='post-view' )
]