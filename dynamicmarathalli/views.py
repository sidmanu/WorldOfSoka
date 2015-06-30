from django.shortcuts import render 
from django.http import HttpResponse

from dynamicmarathalli.models import *


def dm_render(request, template):
	context = {}
	
	return render(request, template, context)

def index(request):
	return dm_render(request, 'dynamicmarathalli/index.html')


def concept_committee(request):
	return dm_render(request, 'dynamicmarathalli/concept.html')

def cultural_committee(request):
	return dm_render(request, 'dynamicmarathalli/cultural.html')

def fd_committee(request):
	return dm_render(request, 'dynamicmarathalli/fd.html')
