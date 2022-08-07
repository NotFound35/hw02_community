from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_COUNT = 10
# Create your views here.


def index(request):
    posts = Post.objects.all()[:POST_COUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POST_COUNT]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
