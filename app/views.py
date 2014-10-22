from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.models import *
from app.forms import *


# Create your views here.

def principal(request, template_name= 'index.html'):
	form = ClientForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, template_name, locals())

def foreaneas(request, template_name = 'foraneas.html'):
	form = SchoolForm(request.POST  or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/foraneas')
	return render(request, template_name, locals())