from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login(request):
	form = AuthenticationForm()
	return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
	return HttpResponse('You are now logged in')


def logout(request):
	auth.logout(request)
	return HttpResponse('You are now logged out')


def invalid(request):
	return HttpResponse('Invalid Login')

