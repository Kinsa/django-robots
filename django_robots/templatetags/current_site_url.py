"""Code from http://fragmentsofcode.wordpress.com/2009/02/24/django-fully-qualified-url/"""

from django import template


register = template.Library()


@register.simple_tag
def current_site_url():
    """Returns fully qualified URL (no trailing slash) for the current site."""
    from django.contrib.sites.models import Site
    from django.conf import settings
    try:
        current_site = Site.objects.get_current()
    except Site.DoesNotExist:
        return ''
    protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
    port     = getattr(settings, 'MY_SITE_PORT', '')
    url = '%s://%s' % (protocol, current_site.domain)
    if port:
        url += ':%s' % port
    return url
