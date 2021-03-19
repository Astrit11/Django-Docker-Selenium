from django.urls import path,re_path
from alpha_help_desk import views

urlpatterns = [
    path('sample', views.API.as_view()),
]