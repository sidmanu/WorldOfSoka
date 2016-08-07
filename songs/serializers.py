from rest_framework import serializers
from songs.models import Song

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('id','title','song_path','lyrics_path')