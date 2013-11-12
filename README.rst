===============
 Django Robots
===============

Installation from Source
========================

::

 $ git clone git@github.com:jbergantine/django-robots.git
 $ cd django-robots
 $ python setup.py install

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following line:

::

 -e git://github.com/jbergantine/django-robots.git#egg=django_robots

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Setup the Project For the Application
=====================================

Add to the project's settings.py file tuple of installed apps: ::

 'django_robots',

In the project's urls.py file add: ::

 url(r'^robots.txt$', include('django_robots.urls')),

Enable the `sites framework`__:

1. Add ``'django.contrib.sites'`` to your ``INSTALLED_APPS`` setting.

2. Define a ``SITE_ID`` setting: 

::

 SITE_ID = 1
 
3. Run ``syncdb``.

From the Django Admin, configure the Domain Name and Display Name for the site, the domain name will be used in the robots.txt file to point to the absolute URL of the site's sitemap.xml file.

Configure the robots.txt Template
=================================

By default the robots.txt template only includes a directive to point to the sitemap at http://site_url/sitemap.xml. This should be removed if the site doesn't have an `XML sitemap`__ for some reason. If you're using virtualenv, to copy the templates from the project in order to make adjustments to them, cd to the root of the django project and execute the following command: ::

 cp -r ../src/django-robots/django_robots/templates/robots templates/robots

__ http://docs.djangoproject.com/en/dev/ref/contrib/sites/#module-django.contrib.sites

__ http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/

Template Tags Installed
=======================

current_site_url
````````````````

Returns a full URL for the current site including custom protocol and port if set (i.e. https://example.com:8080).

Example usage:

::
 
 {% load current_site_url %}
 {% current_site_url %}
