import os
import Statistics
output_dir = "results"

def is_valid_chord(chord):
	return (not (chord == 'N' or chord =='X') and chord)

def normalize_chord_name(chord):
	chord_components = chord.split(':')
	normalized_chord = chord_components[0]

	# chord_qualifier means the min, maj, min7, sus4, etc
	chord_qualifier = (chord_components[1]).strip()
	
	if ('min' in chord_qualifier) or ('maj' in chord_qualifier):
		normalized_chord += helper_min_major_chord_qualifier(chord_qualifier)

	# for chords of non min,maj type. i.e., dim, sus4, 7th chords, etc
	else:
		normalized_chord += chord_qualifier

	return normalized_chord

def helper_min_major_chord_qualifier(chord_qualifier):
	# if the chord is exactly 'min' or 'maj'
	if len(chord_qualifier) == 3:
		if 'min' in chord_qualifier:
			return 'm'
		else:
			return ''

	# for min and maj chords on 7th, 4th note, etc
	elif 'min' in chord_qualifier:
		return 'm' + chord_qualifier[3: len(chord_qualifier)]
	else:
		return chord_qualifier[3: len(chord_qualifier)]

def get_cleaned_chord_name(chord):
	if is_valid_chord(chord):
		return normalize_chord_name(chord)

def extract_chords_info(f, file_name):
	output_file = open(output_dir+"/"+str (file_name)+".txt", 'w')
	for line in f.readlines():
		strs = line.split('\t')
		chord = strs[-1].strip()

		chord = ((get_cleaned_chord_name(chord)))
	
		if not chord == None:
			# print chord
			output_file.write(str (chord) + " ")

def main():
	path="Dataset/kaggle/annotations"
	output_file_name = 1

	print ("=====> [INFO] CHORD EXTRACTION STARTED... <====")

	for directory in os.listdir(path):
		if not directory.startswith("."):
			for file in os.listdir(path+"/"+directory):
				f = open(path+"/"+directory+"/"+file, 'r')
				extract_chords_info(f, output_file_name)
				break
		output_file_name += 1

	print ("=====> [INFO] CHORD EXTRACTION COMPLETE... <====")

def test_normalize():
	normalize_chord_name("A:maj")
	normalize_chord_name("A:min")
	normalize_chord_name("A:min7")
	normalize_chord_name("A:sus4")
	normalize_chord_name("A:maj4")
	normalize_chord_name("A:7")	

if __name__=="__main__":
	main()
	Statistics.GenerateStatistics()
	# test_normalize()