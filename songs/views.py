from django.shortcuts import render 
from django.http import HttpResponse
from django import forms
from django.utils.html import format_html
import sys, traceback

from songs.models import Song, Language
from songs.models import get_most_downloaded_5_songs_list, get_latest_5_songs_list

def get_sidebar_context():
	lang_dict = {}
	lang_list = Language.objects.all()	
	lang_dict['lang_list'] = lang_list
	return lang_dict

def index(request):
	context = get_sidebar_context()
	latest_songs_list = get_latest_5_songs_list()
	context['latest_songs'] = latest_songs_list 

	most_dwld_songs_list = get_most_downloaded_5_songs_list()
	context['most_dwld_songs'] =  most_dwld_songs_list
	return render(request, 'songs/index.html', context)

def contact(request):
	context = get_sidebar_context()
	return render(request, 'songs/contact.html', context)

def lang(request, lang):
	context = get_sidebar_context()
	lang = Language.objects.get(lang_name=lang) 
	if lang:
		song_list = lang.song_set.order_by('title')
		context['song_list'] = song_list
		context['lang'] = lang.lang_name.title()
	return render(request, 'songs/lang.html', context) 

def download(request, song_id):
	context = get_sidebar_context()
	song_id = int(song_id)
	try:
		song = Song.objects.get(pk=song_id)
		song.num_downloads += 1
		song.save()
		context['song'] = song	
		return render(request, 'songs/download.html', context) 

	except:
		traceback.print_exc(file=sys.stdout)
	return HttpResponse('Server Error!!!')

def search(request):
	context = get_sidebar_context()
	if request.method == 'POST':
		string = request.POST['search_string']
	else:
		string = "united sensei"
	context['search_string'] = string 
	tokens = string.split()	
	songs = Song.objects.all()	

	for token in tokens:	
		songs = songs.filter(title__contains=token)

	context['song_list'] = songs
	return render(request, 'songs/search.html', context) 
