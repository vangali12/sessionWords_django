# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
	return render(request, 'sessionWords_app/index.html')

def addItem(request):
	context = {
		'word': request.POST['word'],
		'fontcolor': request.POST['fontcolor'],
		'size': request.POST['big'],
		'date': strftime("%x", gmtime()),
		'time': strftime("%X", gmtime()),
	}
	if 'arr' not in request.session:
		request.session['arr'] = []
		x = request.session['arr']
		x.append(context)
		request.session['arr']
	else:
		x = request.session['arr'] 
		x.append(context)
		request.session['arr'] = x
	return render(request, 'sessionWords_app/index.html')

def clear(request):
	request.session.clear()
	return redirect('/')