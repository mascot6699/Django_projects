from django.shortcuts import render

# Create your views here.

from models import BlogPost
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404

def latest_post(request):
    # import pdb; pdb.set_trace()
    try:
        post = BlogPost.objects.latest('date_posted')
    except BlogPost.DoesNotExist:
        raise Http404
    return render_to_response('blog.html', {'post' : post},context_instance = RequestContext(request))


