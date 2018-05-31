import fileinput
def stats(filename):
    linecount,wordcount,charactercount=0,0,0
    with open(filename,'r+') as file:
        for line in file:
            linecount += 1
            for word in line.split():
                wordcount += 1
                charactercount += len(word)
    print(linecount,wordcount,charactercount)
file=open('samplefile.txt','w+')
file.write('Hello\nI study in\nMSRIT')
file.close()
stats('samplefile.txt')