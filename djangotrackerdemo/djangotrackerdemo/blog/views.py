from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogname(request, blog_id):
    return HttpResponse("You're looking at blog %s." % blog_id)