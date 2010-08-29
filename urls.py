from django.conf.urls.defaults import *
from django-robots.views import robots
    
urlpatterns = patterns('',
    (r'^$', robots, '', 'robots'),
)
