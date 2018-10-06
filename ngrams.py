import os
import operator
import io
import nltk
#nltk.download('punkt')
from nltk import word_tokenize
from nltk.util import ngrams

inp_dir = "inp_data/"

unigram_dict, bigram_dict, trigram_dict, quadgram_dict = {}, {}, {}, {}
unigrams,bigrams,trigrams,quadgrams =[[]], [[]], [[]], [[]]


def build_master_index():
    for file in os.listdir("results/"):
        file_contents = open("results/" + file, 'r', encoding='utf-8').read()
        chords = file_contents.split()
        if len(chords) >0:
            keyNote = chords[0]
            unigram = ngrams(chords,1)
            bigrams = ngrams(chords,2)
            trigrams = ngrams(chords,3)
            quadgrams = ngrams(chords,4)

        construct_dict1(unigram, 1, keyNote)
        construct_dict1(bigrams, 2, keyNote)
        construct_dict1(trigrams, 3, keyNote)
        construct_dict1(quadgrams, 4, keyNote)

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
    if n == 1:
        return unigram_dict
    elif n == 2:
        return bigram_dict
    elif n == 3:
        return trigram_dict
    else:
        return quadgram_dict


def construct_dict1 (tokenList, n, keyNote):
    for indx in range(len(tokenList)):
        if not (indx == len(tokenList) - 1):
            key = tokenList[indx]
            value = tokenList[indx + 1]
        else:
            key = tokenList[indx]
            value = tokenList[0]
            # caveat : overiding keys should not happen. check it
        key = ' '.join(key)
        value = ' '.join(value)
        write_into_result_index(get_dict_name(n), key, value, keyNote)

    newFile = open("unigrams.txt", 'w', encoding='utf-8')
    newFile.write(str(unigram_dict))
    newFile.close()
    newFile = open("bigrams.txt", 'w', encoding='utf-8')
    newFile.write(str(bigram_dict))
    newFile.close()
    newFile = open("trigrams.txt", 'w', encoding='utf-8')
    newFile.write(str(trigram_dict))
    newFile.close()
    newFile = open("quadgrams.txt", 'w', encoding='utf-8')
    newFile.write(str(quadgram_dict))
    newFile.close()

def ngrams(input, n):
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

if __name__ == "__main__":
    build_master_index()
