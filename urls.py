from django.conf.urls.defaults import *
from robots.views import robots
    
urlpatterns = patterns('',
    (r'^$', robots, '', 'robots'),
)
