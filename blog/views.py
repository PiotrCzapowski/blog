from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    post_list=Post.onjects.all()
    return render(request,'blog/index.html',{'post_list':post_list})

def post_detail(request,post):
    post_list=Post.onjects.all()
    post=get_object_or_404(Post, slug=post )
    return render(request,'blog/post_detail.html', {'post_list':post_list,'post':post})
