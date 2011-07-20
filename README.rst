===============
 Django Robots
===============

Installation from Source
========================

::

 $ git clone git@github.com:jbergantine/django-robots.git
 $ cd django-robots
 $ python setup.py install

Setup the Project For the Application
=====================================

Add to the project's settings.py file tuple of installed apps: ::

 'django_robots',

In the project's urls.py file add: ::

 url(r'^robots.txt$', include('django_robots.urls')),

Make sure the `sites framework`__ is configured and enabled (it should be by default). 

Configure the robots.txt Template
=================================

By default the robots.txt template only includes a directive to point to the sitemap at http://site_url/sitemap.xml. This should be removed if the site doesn't have an `XML sitemap`__ for some reason. If you're using virtualenv, to copy the templates from the project in order to make adjustments to them, cd to the root of the django project and execute the following command: ::

 cp -r ../src/django-robots/django_robots/templates/robots templates/robots

__ http://docs.djangoproject.com/en/dev/ref/contrib/sites/#module-django.contrib.sites

__ http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/