from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.


def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(tag__name=cat_name)   # we use __ because cat is a foreign key

    if author_username:
        posts = posts.filter(author__username=author_username)

    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    current_post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    context = {'post': current_post}
    return render(request, 'blog/single-blog.html', context)
