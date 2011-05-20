from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'robots/robots.txt', 'mimetype': 'text/html'}, 'robots'),
)
