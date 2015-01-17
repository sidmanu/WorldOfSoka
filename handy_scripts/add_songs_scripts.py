import os
import re
import sys 
import datetime
import django

#Just change the LANG variable to be of the same name as
#/static/songs/<lang> . It will populate the DB accordingly.
#LANG = 'japanese'
LANG = 'instrumental'

os.environ["DJANGO_SETTINGS_MODULE"] =  "worldofsoka.settings"
django.setup()
from songs.models import Song, Language

def get_file_list(lang):
        files = os.listdir("static/songs/%s"%(lang))
	return files


def rename_song(lang, old_song, new_song_name):
	old_cwd = os.getcwd()
	os.chdir('static/songs/%s/'%lang)
	os.rename(old_song, new_song_name)
	os.chdir(old_cwd)
	print "Renamed %s to %s"%(old_song, new_song_name)

def get_clean_song_name(song_name):
	song_no_blanks = re.sub('\s+', '_', song_name)
	song_clean = re.sub('[^A-Za-z0-9_\.]+', '', song_no_blanks)
	song = song_clean.lower()	
	return song	

def get_full_song_path(lang, song_path):
	return 'songs/%s/%s'%(lang,
		song_path)

def get_song_title_from_song_filename(filename):
	song_name = re.sub('_', ' ', filename)
	song_name = song_name.replace('.mp3', '')
	return song_name.title()

def get_Language_obj_by_name(name):
	langs = Language.objects.all()
	for lang in langs:
		 if lang.lang_name == name:
			return lang
	print "Couldn't find language!"
	sys.exit(1)

def main():
	lang_obj = get_Language_obj_by_name(LANG)
        song_path_list = get_file_list(LANG)

	if not song_path_list:
		print "No files found!"
		sys.exit(1)	

	#rename files to have conventional file_naming_conventions.mp3
	for song in song_path_list:
		new_song_name = get_clean_song_name(song)
		rename_song(LANG, song, new_song_name)

	#now that file names have  changed, read dir again
        song_path_list = get_file_list(LANG)
	for song in song_path_list:
		song_path = get_full_song_path(LANG, song)
		song_title = get_song_title_from_song_filename(song)
		s = Song(title = song_title,
			song_path = song_path,
			lang = lang_obj,
			upload_date = datetime.datetime.now(),
			num_downloads = 0,
			lyrics_path = 'invalid')

		s.save()

	#print songs	


if __name__ == "__main__":
        main()

