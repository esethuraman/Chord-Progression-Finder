import os
import kaggleDataExtractor as extractor

directory = "Dataset/ArtistLabel/uspopLabels"

output_file_name = 1
for album_name in os.listdir(directory):
	for song_name in os.listdir(directory+'/'+album_name):
		for chord_details_file_name in os.listdir(directory+'/'+album_name+'/'+song_name):
			f = open(directory + "/" + album_name+"/"+song_name+"/"+chord_details_file_name, 'r')
			extractor.extract_chords_info(f, 'album'+ str (output_file_name))
			output_file_name +=  1
			
			print album_name