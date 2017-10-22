import os

files = os.listdir(os.path.dirname(__file__) +'/' +'rawWordsFreEachNews')
for i in range(0,len(files)):
    output_file = os.path.dirname(__file__)+'/finalWordsFreEachNews' +'/' + files[i]
    rawData = open(os.path.dirname(__file__)+'/rawWordsFreEachNews' + '/' + files[i])
    stopWords = open(os.path.dirname(__file__)+'/stopWords.txt')
    rawDataList= []
    rawDataFre = [] # record how many time this word appear
    stopWordsList = []
    finalDataList = []
    finalDataFre = []
    while 1:
        line = rawData.readline()
        if not line:
            break;
        else:
            rawDataList.append(line.split()[1])
            rawDataFre.append(line.split()[0])
    while 1:
        line = stopWords.readline()
        if not line:
            break;
        else:
            stopWordsList.append(line.split()[0])

    for i in range(0,len(rawDataList)):
        count = 0
        for j in range(0,len(stopWordsList)):
            if(rawDataList[i] != stopWordsList[j]):
                count += 1
        if count == len(stopWordsList):
            finalDataList.append(rawDataList[i])
            finalDataFre.append(rawDataFre[i])
        
    file = open(output_file,'a')
    for i in range(0,len(finalDataList)):
        file.write(finalDataFre[i])
        file.write(" ")
        file.write(finalDataList[i])
        file.write("\n")


        
