from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .visited import Visited
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def index(request):
    post_list=Post.objects.all().order_by('-publish')
    paginator=Paginator(post_list,6)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        post_list = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,'blog/list_ajax.html',{'section':'post_list','post_list': post_list})
    else:
        return render(request, 'blog/index.html', {'section':'post_list','post_list': post_list})

def post_detail(request,post):
    visited=Visited(request)
    post_list=Post.objects.all().order_by('-publish')[:5]
    post=get_object_or_404(Post, slug=post )
    # post.visitors_counter += 1
    # post.save()
    visited.add(post)
    return render(request,'blog/post_detail.html', {'post_list':post_list,'post':post})
