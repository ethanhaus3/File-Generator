inputFile = open('names.csv','r')
outputFile = open('girlnames.txt','w')
outputFile2 = open('boynames.txt','w')
stringList = []
for i in inputFile:

    stringList = i.split(",")
    girl = stringList[2]
    boy = stringList[1]
    outputFile.write(girl + "\n")
    outputFile2.write(boy + "\n")


