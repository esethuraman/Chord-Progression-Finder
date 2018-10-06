
def evaluationFunction(inputList,keyNote):
    lengthOfInput = len(inputList)
    nextNoteSeqValues = {}
    indexFile = get_Ngram_FileName(lengthOfInput)
    file_contents = open(indexFile, 'r', encoding='utf-8')
    ngramDict = eval(file_contents.read())
    inputString = ' '.join(inputList)
    #print(inputString)
    if inputString in ngramDict.keys():
        nextNoteSeqValues = (ngramDict[inputString])

    else:
        indexFile = get_Ngram_FileName(2)
        file_contents = open(indexFile, 'r', encoding='utf-8')
        ngramDict = eval(file_contents.read())
        inputString = ' '.join(inputList)
        if inputString in ngramDict.keys():
            nextNoteSeqValues = (ngramDict[inputString])
    scoreSeqDict = {}

    for key, innerDict in nextNoteSeqValues.items():
        score = 1
        if key == keyNote:
            for seq, frequency in innerDict.items():
                if seq in scoreSeqDict:
                    score = frequency * 0.6 + 2;
                scoreSeqDict[seq] = score

        else:
            for seq, frequency in innerDict.items():
                if seq in scoreSeqDict:
                    score = frequency * 0.6;
                scoreSeqDict[seq] = score
    RankedOutput = sorted(scoreSeqDict.items(), key=lambda kv: kv[1], reverse = True)
    (RankedOutput,indexToBeDeleted) = cleanup_results(RankedOutput, inputList)
    for indexDel in indexToBeDeleted:
        RankedOutput[indexDel]= ('','')

    for eachList in RankedOutput:
        if eachList == ('',''):
            RankedOutput.remove(eachList)

    if len(RankedOutput) <= 5:
        return RankedOutput
    else:
        return RankedOutput[:5]

def cleanup_results(cleanOutput, inputList):
    indexToBeDeleted = []
    index =0
    for (seq, score) in cleanOutput:
        seqList = seq.split()
        if seqList[0]== inputList[len(inputList) - 1]:
            indexToBeDeleted.append(index)
        cleanTupleList = remove_duplicate_chords(cleanOutput)
        index+=1
    return (cleanTupleList, indexToBeDeleted)

def is_Unique_String(seqList):
    for i in range(len(seqList)-1):
        if seqList[i] == seqList[i+1]:
            return False
    return True

def get_Ngram_FileName(lengthOfInput):
    if lengthOfInput ==1:
        return "unigrams.txt"
    elif lengthOfInput ==2:
        return "bigrams.txt"
    elif lengthOfInput ==3:
        return "trigrams.txt"
    else:
        return "quadgrams.txt"

def remove_duplicate_chords(tuple_list):
    result_tuple_lst = []
    for tupl in tuple_list:
        chord_seq = tupl[0]
        chords = chord_seq.split()
        prev = chords[0]
        result_chords = [prev]

        for i in range(1, len(chords)):
            chord = chords[i]
            if chord != prev:
                result_chords.append(chord)
                prev = chord
        chords_as_str = ' '.join(result_chords)
        result_tuple_lst.append((chords_as_str, tupl[1]))
    return result_tuple_lst


a = evaluationFunction(['Am','Dm'], 'C')
print (a)