Installation
============

Make sure that the robots application is on the python path
-----------------------------------------------------------

Using virtualenvwrapper run the following in a shell:
`add2virtualenv /path/to/directory_above_robots/`

Using bash:
edit the ~/.bash_profile or similar file, add to it the following line:
`export PYTHONPATH=$PYTHONPATH:/path/to/directory_above_robots/`

Setup the project for the application
-------------------------------------

Add to the project's settings.py file tuple of installed apps:
`'robots',`

In the project's urls.py file add:
`(r'^robots.txt$', include('robots.urls')),`

Make sure the [sites framework](http://docs.djangoproject.com/en/dev/ref/contrib/sites/#module-django.contrib.sites) is configured and enabled (it should be by default). 

Configure the robots.txt template
---------------------------------

By default the robots.txt template only includes a directive to point to the sitemap at http://site_url/sitemap.xml. This should be removed if the site doesn't have an [XML sitemap](http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/) for some reason.