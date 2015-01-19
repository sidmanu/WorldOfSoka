from django.db import models

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
