#def calculateRank():


def evaluationFunction(inputList, keyNote):
    lengthOfInput = len(inputList)

    indexFile = get_Ngram_FileName(lengthOfInput)
    file_contents = open(indexFile, 'r', encoding='utf-8')
    ngramDict = eval(file_contents.read())
    inputString = ' '.join(inputList)
    print(inputString)
    if inputString in ngramDict.keys():
        print(ngramDict[inputString])


def get_Ngram_FileName(lengthOfInput):
    if lengthOfInput ==1:
        return "unigrams.txt"
    elif lengthOfInput ==2:
        return "bigrams.txt"
    elif lengthOfInput ==3:
        return "trigrams.txt"
    else:
        return "quadgrams.txt"

if __name__ == "__main__":
    evaluationFunction(['Bbm','Ebm'], 'Bbm')