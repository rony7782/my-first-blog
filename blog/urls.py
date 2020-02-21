from django.urls import path
from . import views

urlpatterns = [
    path('rony7782.github.io', views.post_list, name='post_list'),
]
