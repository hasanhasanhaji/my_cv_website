from cvweb.views import index_view, about_view, contact_view,element_view, portfolio_view, service_view
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('url',view)
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('element/', element_view, name='element'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('service/', service_view, name='service'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

