from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})
