from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
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
        return render(request, 'home/about.html')

class ForumView(View):
    def get(self, request):
        return render(request, 'home/forum.html')