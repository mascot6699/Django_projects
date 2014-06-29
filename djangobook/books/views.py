from django.db.models import Q
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from models import Book
from forms import *

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
		Q(title__icontains=query) |
		Q(authors__first_name__icontains=query) |
		Q(authors__last_name__icontains=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("results.html", {"results": results,"query": query })


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic 			= form.cleaned_data['topic']
			message 		= form.cleaned_data['message']
			sender 			= form.cleaned_data.get('sender', 'noreply@example.com')
			send_mail('Feedback from your site, topic: %s' % topic, message, sender,['umangshucool@gmail.com'])
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial={'sender': 'user@example.com'})
	return render_to_response('contact.html', {'form': form})

def contactus(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic 			= form.cleaned_data['topic']
			message 		= form.cleaned_data['message']
			sender 			= form.cleaned_data.get('sender', 'noreply@example.com')
			send_mail('Feedback from your site, topic: %s' % topic, message, sender,['umangshucool@gmail.com'])
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial={'sender': 'user@example.com'})
	return render_to_response('contactus.html', {'form': form})


def addpublisher(request):
	if request.method == 'POST':
		form = PublisherForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/addpublisher/thanks/')
	else:
		form = PublisherForm()
		return render_to_response('addpublisher.html', {'form': form})

def publisherthanks(request):
	return render_to_response('thanks.html')