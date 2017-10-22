import os
path = os.path.dirname(__file__)
print path
inputfile1 = path + '/wordsFreOfAllNews.txt'
inputfile2 = path + '/1.txt'
outputfile = path + '/result.txt'
file1 = open(inputfile1)
file2 = open(inputfile2)
words = []
values = []
subset = []
count = []
while 1:
    line = file1.readline()
    if not line:
        break
    else:
        words.append(line.split()[1])
        count.append(line.split()[0])
while 1:
    #print line
    line = file2.readline()
   # print line 
    if not line:
        break
    else:
       # print line
       # print len(line.split())
        if(len(line.split()) != 2):
            if(len(subset) != 0):
               # print line
               # print "nihao"
               # print " "
               # print " "
                values.append(subset)
                subset = []
            subset.append(line.split()[2])
        else:
           # print line + "hello"
           # print "hello"
            subset.append(line.split()[0])
values.append(subset)
#print len(words)
#print len(values)
ff = 0
for i in range(0,len(words)):
    synonym = values[i]
    for j in range(0,len(words)):
        for n in range(0,len(synonym)):
            if(words[j] == synonym[n]):
                words[j] = "deleted"
                ff += 1
                break

result = {}
for i in range(0,len(words)):
    if(words[i] != "deleted"):
        result[words[i]] = count[i]
file = open(outputfile,'a')
for key in result:
    file.write(result[key])
    file.write(" ")
    file.write(key)
    file.write("\n")
#print ff
        
    
    
