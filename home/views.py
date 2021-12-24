from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import Comment
from home.forms import CommentForm
# Create your views here.

class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        contex = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'form': AuthenticationForm
        }
        return render(request, 'home/index.html', contex)

class AboutView(View):
    def get(self, request):
        contex = {
            'form': AuthenticationForm
        }
        return render(request, 'home/about.html', contex)

class ForumView(View):
    
    def get(self, request):
        #print(request.user)
        comments = Comment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        print(CommentForm())
        contex = {
            'comments': comments,
            'comment_form': comment_form,
            'form': AuthenticationForm
        }
        return render(request, 'home/forum.html', contex)
    
    def post(self, request):
        comment = Comment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('forum'))

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        return redirect(reverse('forum'))


#class CommentCreateView(LoginRequiredMixin, View):
#    def post(self, request):
#        comment = Comment(text=request.POST['comment'], owner=request.user)
#        comment.save()
#        return redirect(reverse('home:forum'))

class CommentDeleteView(LoginRequiredMixin, View):
    model = Comment
    #template_name = 'home/forum.html' #Probar esto

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect(reverse('forum'))

    #def get_success_url(self):
    #    forum = self.object.forum
    #    return reverse('forum')

