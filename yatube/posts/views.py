from django.shortcuts import render, get_object_or_404

from .models import Post, Group

post_count = 10
# Create your views here.


def index(request):
    posts = Post.objects.all()[:post_count]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:post_count]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
