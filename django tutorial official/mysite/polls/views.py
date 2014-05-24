# Create your views here.
from django.http import HttpResponse, HttpRequest , HttpResponseRedirect
#from django.template import RequestContext, loader
#from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render , get_object_or_404
from django.views import generic
from polls.models import Poll, Choice

"""
def us1index(request):
    return HttpResponse("<html><body><h1>okay!</h1></body></html>")

def us1detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def us1results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def us1vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def usindex(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:3]
    output = '<br>'.join([p.question for p in latest_poll_list])
    return HttpResponse("the latest 3 polls are <br><br>" + output)

def us2index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:3]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:3]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
"""


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last three published polls."""
        return Poll.objects.order_by('-pub_date')[:3]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'