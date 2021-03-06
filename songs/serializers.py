from rest_framework import serializers
from songs.models import Song, Language


class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('id','title','song_path','lyrics_path','lang','num_downloads')

class SongDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('id','title','song_path','lyrics_path','lang','lyrics_text')



