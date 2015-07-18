from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *

# Create your views here.


def home(request):
    return render(request, 'reports/home.html')


def submit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/complete/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()
    return render(request, 'reports/form.html',{'form': form})



def complete(request):
    return render(request, 'reports/complete.html')

def connect(request):
    return render(request, 'reports/underconstruction.html')

def track(request):
    return render(request, 'reports/underconstruction.html')

def about(request):
    return render(request, 'reports/about.html')

