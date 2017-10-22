import os
files = os.listdir(os.path.dirname(__file__) + '/finalWordsFreEachNews')
fre_words = {}
for i in range(0,len(files)):
    rawData = open(os.path.dirname(__file__)+'/finalWordsFreEachNews' + '/' + files[i])
    count = 5
    while count > 0:
        line = rawData.readline()
        if not line:
            break;
        else:
            fre_words.setdefault(line.split()[1],0)
            fre_words[line.split()[1]] = fre_words[line.split()[1]] + int(line.split()[0])
        count = count - 1
sorted_fre_words = sorted(fre_words.items(),key = lambda item:item[1])
#print sorted_fre_words
output_file = os.path.dirname(__file__) + '/wordsFreOfAllNews.txt'
file = open(output_file,'a')
for i in range(0,len(sorted_fre_words)):
    file.write('%d' %sorted_fre_words[i][1])
    file.write(" ")
    file.write(sorted_fre_words[i][0])
    file.write("\n")
    
