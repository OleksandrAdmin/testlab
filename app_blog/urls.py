# app_blog/urls.py
from django.urls import path
from mysite.app_blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
