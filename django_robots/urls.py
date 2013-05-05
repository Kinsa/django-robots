from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', 
        {'template': 'robots/robots.txt', 'mimetype': 'text/plain'}, 'robots'),
)
