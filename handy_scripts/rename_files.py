import os
import re
#Renames all the files in curdir into filenames in lowercase, separated by _

def get_file_list():
        files = os.listdir(".")
	return files


def rename_song( old_song, new_song_name):
	os.rename(old_song, new_song_name)
	print "Renamed %s to %s"%(old_song, new_song_name)

def get_clean_song_name(song_name):
	song_no_blanks = re.sub('\s+', '_', song_name)
	song_clean = re.sub('[^A-Za-z0-9_\.]+', '', song_no_blanks)
	song = song_clean.lower()	
	return song	

def main():
        lyrics_path_list = get_file_list()

	if not lyrics_path_list:
		print "No files found!"
		sys.exit(1)	

	#rename files to have conventional file_naming_conventions.mp3
	for item in lyrics_path_list:
		new_file_name = get_clean_song_name(item)
		rename_song(item, new_file_name)


if __name__ == "__main__":
        main()

