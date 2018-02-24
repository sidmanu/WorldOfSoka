from django.shortcuts import render 
from django.http import HttpResponse
from django import forms
from django.utils.html import format_html
from rest_framework.permissions import IsAdminUser
from rest_framework import filters 
from rest_framework.response import Response
from rest_framework.decorators import api_view
import django_filters

import sys, traceback

from rest_framework import generics

from songs.serializers import * 
from songs.models import Song, Language, Stats
from songs.models import get_most_downloaded_5_songs_list, get_latest_5_songs_list
from songs.models import get_3_random_songs, get_all_tags, get_songs_by_tag



class SearchSongView(generics.ListAPIView):
	serializer_class = SongSerializer

	def get_queryset(self):
		string = self.kwargs['search_string']
		tokens = string.split()	
		songs = Song.objects.all()	
		for token in tokens:	
			songs = songs.filter(title__contains=token)
		return songs 


class LangView(generics.ListAPIView):
	serializer_class = SongSerializer

	def get_queryset(self):
		lang_name = self.kwargs['lang_name']
		try:
			lang = Language.objects.filter(lang_name__contains=lang_name)
		except:
			lang = Language.objects.get(pk=1)

		return Song.objects.filter(lang=lang)

@api_view(['GET'])
def song_info(request, song_id):

	try:
		song = Song.objects.filter(pk=song_id)
	except:
		song = Song.objects.filter(pk=23)

	serializer = SongDetailSerializer(song, many=True)
	song = serializer.data

	return Response({"songs": song})

class SongView(generics.ListAPIView):
	queryset = Song.objects.all()
	model = Song
	serializer_class = SongSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('lyrics_path','lang',)

def mark_site_visit():
	try:
		stats_obj = Stats.objects.get()
	except:
		stats_obj = Stats(total_visitors=0)

	stats_obj.total_visitors += 1
	stats_obj.save()


def get_stats():
	stats = {}
	try:
		stats_obj = Stats.objects.get()
		stats['total_visitors'] = stats_obj.total_visitors
	except:
		stats['total_visitors'] = 0
	return stats

def get_sidebar_context():
	mark_site_visit()
	lang_dict = {}
	lang_list = Language.objects.all()	
	lang_dict['lang_list'] = lang_list
	lang_dict['stats'] = get_stats()
	return lang_dict

def index(request):
	context = get_sidebar_context()
	tags = get_all_tags()
	context['tags'] = tags
	latest_songs_list = get_latest_5_songs_list()
	context['latest_songs'] = latest_songs_list 
	context['random_songs'] = get_3_random_songs()

	most_dwld_songs_list = get_most_downloaded_5_songs_list()
	context['most_dwld_songs'] =  most_dwld_songs_list
	return render(request, 'songs/index.html', context)

def contact(request):
	context = get_sidebar_context()
	return render(request, 'songs/contact.html', context)

def update_lyrics(request):
	context = get_sidebar_context()
	song_list = [] 
	languages = Language.objects.all()
	for lang in languages:
		lang_info = {}
		lang_info['language'] = lang.lang_name
		lang_info['song_list'] = []
		songs = Song.objects.filter(lang=lang).order_by('title')
		for song in songs:
			if 'invalid' in song.lyrics_path:
				lang_info['song_list'].append(song)
				
		song_list.append(lang_info)
	context['song_list'] = song_list 
	return render(request, 'songs/update_lyrics.html', context) 


def lang(request, lang):
	context = get_sidebar_context()
	lang = Language.objects.get(lang_name=lang) 
	if lang:
		song_list = Song.objects.filter(lang=lang)
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

def tag(request, tag):
	context = get_sidebar_context()
	songs = get_songs_by_tag(tag)	
	context['tag'] = tag
	context['song_list'] = songs
	return render(request, 'songs/song_by_tag.html', context) 

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
