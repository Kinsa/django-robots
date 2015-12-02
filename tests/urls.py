from django.conf.urls import include, url

urlpatterns = [
    url(r'^robots.txt', include('django_robots.urls')),
]
