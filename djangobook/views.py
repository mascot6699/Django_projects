from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request,offset):
	offset = int(offset)
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hours, the time will be %s. </body></html>" % (offset,now )
	return HttpResponse(html)

def hours_behind(request,offset):
	offset = int(offset)
	now = datetime.datetime.now() - datetime.timedelta(hours=offset)
	return render_to_response('hours_behind.html', {'current_date': now, 'offset':offset})

