from django.db import models
import random

class Stats(models.Model):
	total_visitors = models.IntegerField(default=0)

class Language(models.Model):
	lang_name = models.CharField(max_length=30)	
	
	def __unicode__(self):
		return self.lang_name

class Song(models.Model):
	title = models.CharField(max_length=50)
	lang = models.ForeignKey(Language) 
	upload_date = models.DateTimeField('date uploaded')
	keywords = models.TextField(blank=True)
	song_path = models.CharField(max_length=70)
	lyrics_path = models.CharField(max_length=70)
	num_downloads = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

def get_latest_5_songs_list():
	return Song.objects.order_by('-upload_date')[:5]

def get_most_downloaded_5_songs_list():
	return Song.objects.order_by('-num_downloads')[:5]

def get_3_random_songs():
	max_count = Song.objects.count()
	random_1 = random.randint(0, max_count - 1)
	random_2 = random.randint(0, max_count - 1)
	random_3 = random.randint(0, max_count - 1)
	all_songs = Song.objects.all()
	songs_list = [] 
	songs_list.append(all_songs[random_1])
	songs_list.append(all_songs[random_2])
	songs_list.append(all_songs[random_3])
	return songs_list

def get_all_tags():
	tags = set()
	all_songs = Song.objects.all()
	for song in all_songs:
		keywords_list = song.keywords.split()
		for keyword in keywords_list:
			tags.add(keyword)
	tags = list(tags)
	return tags

def get_songs_by_tag(tag):
	try:
		songs = Song.objects.filter(keywords__contains=tag)
		return songs
	except:
		return []
