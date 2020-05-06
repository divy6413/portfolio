from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
	blog=Blog.objects
	return render(request, 'blogs/allblogs.html',{'blogs':blog})

def detail(request,blog_id):
	det_blog=get_object_or_404(Blog,pk=blog_id)
	return render(request,'blogs/detail.html',{'blog':det_blog})