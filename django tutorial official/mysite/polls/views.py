# Create your views here.
from django.http import HttpResponse
from polls.models import Poll


def index(request):
    return HttpResponse("<html><body><h1>okay!</h1></body></html>")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def usindex(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:3]
    output = '<br>'.join([p.question for p in latest_poll_list])
    return HttpResponse("the latest 3 polls are <br><br>" + output)
