from django.shortcuts import render 
from django.http import HttpResponse

from dynamicmarathalli.models import *


def dm_render(request, template):
	context = {}
	template = 'myDistrict/' + template	
	return render(request, template, context)

def index(request):
	return dm_render(request, 'index.html')


def concept_committee(request):
	return dm_render(request, 'concept.html')

def cultural_committee(request):
	return dm_render(request, 'cultural.html')

def fd_committee(request):
	return dm_render(request, 'fd.html')
