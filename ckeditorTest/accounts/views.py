from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.template import RequestContext
from django.views.generic import View
from accounts.forms import RegistrationForm, CkEditorForm


class RegisterView(View):

    def post(self, request):
        form = RegistrationForm(request.POST)
        print 'In Register View --- Post'
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email'],
                #role = form.cleaned_data['role'],
            )
            user.save()
            return HttpResponseRedirect('/register/success/')

        variables = RequestContext(request, {'form' : form })
        return render_to_response('registration/register.html', variables,)

    def get(self, request):
        form = RegistrationForm()
        print 'in Register View --- Get'
        variables = RequestContext(request, {'form' : form })
        return render_to_response('registration/register.html', variables,)


class RegisterSuccessView(View):

    def get(self, request):
        print 'hi Register Success View get'
        return render_to_response('registration/success.html',)


class LogoutPageView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class HomeView(View):

    def get(self, request):

        ckform = CkEditorForm()
        print 'In Home View'
        return render_to_response('home.html',{'user' : request.user , 'ckform' : ckform})