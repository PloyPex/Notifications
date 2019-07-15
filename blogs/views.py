from django.shortcuts import render

from .models import Blog

def home_view(request):
	return render(request, 'blogs/home.html')

def list_view(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/list.html', {'blogs': blog})

def detail_view(request, id):
	blog = Blog.objects.get(id=id)
	return render(request, 'blogs/detail.html', {'blog': blog})
