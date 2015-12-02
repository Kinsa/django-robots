import django

if django.VERSION < (1, 9):
    from django.conf.urls import patterns

from django.conf.urls import url

from django.views.generic import TemplateView

urls = [
    url(r'^$', TemplateView.as_view(template_name='robots/robots.txt', content_type='text/plain'), name='robots'),
]

if django.VERSION < (1, 9):
    urlpatterns = patterns('',
        [url_i for url_i in urls]
    )
else:
    urlpatterns = urls
