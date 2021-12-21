from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forum/', views.ForumView.as_view(), name='forum'),
    path('about/', views.AboutView.as_view(), name='about'),
]