import os

def GenerateStatistics():

    allFiles = os.listdir("results")
    fileChordPercent ={}
    for fileName in allFiles:
        chordPercentage = {}
        file_contents = open("results/"+ fileName, 'r', encoding = 'utf-8').read()
        chords = file_contents.split()
        fileLength = len(chords)
        for chord in chords:
            if chord in chordPercentage:
                chordPercentage[chord] += 1
            else:
                chordPercentage[chord] = 1

        for key, value in chordPercentage.items():
            chordPercentage[key] = value / fileLength

        fileChordPercent[fileName] = chordPercentage

    filename = "Statistics"+".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(fileChordPercent))
    newFile.close()


