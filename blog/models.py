from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):  # create class for tags
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/def.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, default='')
    content = models.TextField()
    tag = models.ManyToManyField(Category, )
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):  # a function that shows return value in admin page instead of object
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
        
