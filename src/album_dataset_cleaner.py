import os
import kaggleDataExtractor as extractor

directory = "Dataset/ArtistLabel/uspopLabels"

for album_name in os.listdir(directory):
	for song_name in os.listdir(directory+'/'+album_name):
		for chord_details_file_name in os.listdir(directory+'/'+album_name+'/'+song_name):
			if '.svl' in chord_details_file_name:
				os.remove(directory+'/'+album_name+'/'+song_name+'/'+chord_details_file_name)