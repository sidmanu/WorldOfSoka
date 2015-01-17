from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from songs.models import Song

class SongFileBindingTests(TestCase):

	def test_song_and_lyrics_file_paths_are_correct(self):
		""" if a file doesn't exist, 
		the test should fail"""
		#couldn't get this working :(
		self.assertEqual(False, True)
