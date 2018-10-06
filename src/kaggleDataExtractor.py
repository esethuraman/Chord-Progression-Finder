import os

output_dir = "results"

def is_valid_chord(chord):
	return (not (chord == 'N' or chord =='X') and chord)

def normalize_chord_name(chord):
	chord_components = chord.split(':')
	normalized_chord = chord_components[0]
	if 'min' in (chord_components[1]):
		normalized_chord += 'm'

	return normalized_chord



def get_cleaned_chord_name(chord):
	if is_valid_chord(chord):
		return normalize_chord_name(chord)

def extract_chords_info(f, file_name):
	output_file = open(output_dir+"/"+str (file_name)+".txt", 'w')
	for line in f.readlines():
		strs = line.split('\t')
		chord = strs[-1].strip()
		
		chord = ((get_cleaned_chord_name(chord)))
		# print chord
		if not chord == None:
			output_file.write(str (chord) + " ")

def main():
	path="Dataset/kaggle/annotations"
	output_file_name = 1
	for directory in os.listdir(path):
		if not directory.startswith("."):
			for file in os.listdir(path+"/"+directory):
				f = open(path+"/"+directory+"/"+file, 'r')
				extract_chords_info(f, output_file_name)
				break
		output_file_name += 1

if __name__=="__main__":
	main()