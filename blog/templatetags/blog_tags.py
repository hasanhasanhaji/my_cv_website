from django import template
from blog.models import Post, Category
from django.utils import timezone
from django.shortcuts import get_object_or_404
register = template.Library()


@register.inclusion_tag('blog/blog-post-categories.html')  # it decorates the html file we want to load
def postcategories():  # this function will be used in blog.html to load blog-post-cat.html
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()

    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(tag=name).count()
    return {'categories': cat_dict}


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}