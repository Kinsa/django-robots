from django.template import Context, loader
from django.conf import settings
from django.http import HttpResponse

def robots(request):
	t = loader.get_template('robots.txt')
	c = Context()
	return HttpResponse(t.render(c), mimetype="text/plain")