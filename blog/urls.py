from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    # path('url',view)
    path('', blog_view, name='index'),
    path('single/', blog_single, name='single'),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)