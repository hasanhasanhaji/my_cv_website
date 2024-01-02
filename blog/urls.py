from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    # path('url',view)
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('author/<str:author_username>', blog_view, name='author'),

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)