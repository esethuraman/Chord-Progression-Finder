import os
import io
import nltk
# nltk.download()
from nltk import word_tokenize
from nltk.util import ngrams
inp_dir = "inp_data/"

unigram_dict , bigram_dict, trigram_dict, quadgram_dict = {}, {}, {}, {}

def build_master_index():
	for chord_info in os.listdir(inp_dir):
		with open(inp_dir +"/" + chord_info, 'rb') as f:
			# f.encode(-8').strip()
			# chords_list = f
			lines = (f.readlines())
			sub_lines = (lines[0].decode("ascii", 'ignore')).split('    ')
			print(sub_lines[0].strip())
			# populate_index(chords_list)
			# print( chords_list)

def populate_index(chords_list):
	# 2nd arg is the 'n' in n-gram based on which indices are to be built
	scale = chords_list[0]
	# build_index(chords_list, 1, scale)
	build_index(chords_list, 2, scale)
	# build_index(chords_list, 3, scale)
	# build_index(chords_list, 4, scale)

def build_index(chords_list, n, scale):
	n_so_far = 0
	key_string = ''
	lst_indx = 0
	result_indx = {}
	ngramsToken = generate_ngramsToken(chords_list,n)
	print( ngramsToken)
	# for chord in chords_list:
	# 	n_so_far += 1
	# 	if n_so_far <= n:
	# 		key_string = ' '+chord
	# 		if lst_indx < len(chords_list):
	# 			value_string = ' '+chords_list[lst_indx]
	# 	else:
	# 		write_into_result_index(get_dict_name(n), key_string, value_string, scale )
	# 		n_so_far = 0
	# 		key_string = ''
	# 		value_string = ''
	# 	lst_indx += 1

def generate_ngramsToken(chords_list,n):
	for chord in chords_list:
		tokens = nltk.word_tokenize(chord)
		print( ngrams(tokens, n))
	# return ngramsToken
	return None

def write_into_result_index(output_dict, key_string, value_string, scale):
	
	if key_string in output_dict.keys():
		first_inner_dict = output_dict[key_string]
		if scale in first_inner_dict:
			second_inner_dict = first_inner_dict[scale]
			if value_string in second_inner_dict.keys():
				output_dict[key_string][scale][value_string] += 1
			else:
				 output_dict[key_string][scale][value_string] = 1
		else:
			output_dict[key_string][scale] = {value_string: 1}
	else:
		output_dict[key_string] = {scale: {value_string: 1}}


def get_dict_name(n):
	if n==1:
		return unigram_dict
	elif n==2:
		return bigram_dict
	elif n==3:
		return trigram_dict
	else:
		return quadgram_dict

if __name__=="__main__":
	build_master_index()
	# print( bigram_dict)