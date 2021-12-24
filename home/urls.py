from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forum/', views.ForumView.as_view(), name='forum'),
    path('comment/<int:pk>/delete', 
        views.CommentDeleteView.as_view(), name='forum_comment_delete'),
    path('about/', views.AboutView.as_view(), name='about'),
]