from cvweb.views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cvweb'
urlpatterns = [
    # path('url',view)
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('element/', element_view, name='element'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('service/', service_view, name='service'),
    path('newsletter/', newsletter_view, name='newsletter')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

