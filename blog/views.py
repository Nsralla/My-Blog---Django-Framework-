from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def get_date(post):
    return post['date']

def index(request):
    posts = Post.objects.all().order_by('-date')[:3]
    return HttpResponse(render(request,'blog/index.html',{'posts':posts}))

def all_posts(request):
    posts = Post.objects.all()
    return HttpResponse(render(request, 'blog/all-posts.html',{'posts':posts}))

def post_details(request, slug):
    post = get_object_or_404(Post,slug=slug)
    # get specifc post
    # post = next(post for post in posts if post.slug == slug)
    return HttpResponse(render(request, 'blog/post-details.html' ,{'post': post, 
                                                                   'tags':post.tags.all()}))
