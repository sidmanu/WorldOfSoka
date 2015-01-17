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
	context['latest_songs_list_html'] =  get_html_output_for_song_list(latest_songs_list)

	most_dwld_songs_list = get_most_downloaded_5_songs_list()
	context['most_dwld_songs_list_html'] =  get_html_output_for_song_list(most_dwld_songs_list)
	return render(request, 'songs/index.html', context)

def contact(request):
	context = get_sidebar_context()
	return render(request, 'songs/contact.html', context)

def get_html_output_for_song_list(song_list):
	if len(song_list) == 0:
		return ""
	html_op = "<ul>"
	for song in song_list: 
		html_op += """<li>
			<div id='songtile'>
			%(song_title)s	
			<br/>
			<object width='200' height='20' bgcolor='black' data='/static/dewplayer.swf?son=/static/%(song_path)s&amp;autoplay=0&amp;autoreplay=0' type='application/x-shockwave-flash'>  
			</object>
			<a href='/songs/download/%(song_id)s/'>Download</a>
			</div>
		</li>"""%{'song_title': song.title, 'song_path': song.song_path,
					'song_id': song.id}

	html_op += "</ul>"
	return format_html(html_op)

def lang(request, lang):
	context = get_sidebar_context()
	lang = Language.objects.get(lang_name=lang) 
	if lang:
		song_list = lang.song_set.all()
		context['song_list_html'] = get_html_output_for_song_list(song_list)
		context['lang'] = lang
	return render(request, 'songs/lang.html', context) 

def download(request, song_id):
	context = get_sidebar_context()
	song_id = int(song_id)
	strbuf = ''
	try:
		song = Song.objects.get(pk=song_id)
		song.num_downloads += 1
		song.save()
		context['song'] = song	
		strbuf += "song %s downloaded %d times"%(song.title, song.num_downloads)
		#return HttpResponse(strbuf)
		return render(request, 'songs/download.html', context) 

	except:
		traceback.print_exc(file=sys.stdout)
		strbuf +="Song %d not found!"%song_id
	return HttpResponse(strbuf)
