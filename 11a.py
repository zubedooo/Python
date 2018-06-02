dictionary = dict()
def AddWord():
    global dictionary
    word, meaning = input('Enter word '),input('Enter its meaning ')
    dictionary[word] = meaning
def SearchWord():
    global dictionary
    search = input('Enter Word to search ')
    for word,meaning in dictionary.items():
        if word==search:
            print(meaning)
def DisplayWordsWithSameMeaning():
    search = input('Enter meaning ')
    for word,meaning in dictionary.items():
        if search == meaning:
            print(word,end = ' ')
    print(' ')
def RemoveEntry():
    search = input('Enter word to delete ')
    if dictionary.get(search,None) != None:
        del(dictionary[search])
    else:
        print('Word not found ')
def Sort():
    print('\nWords in a sorted list are\n',sorted(dictionary,key = lambda x: x[0]))

while True:
    ch = int(input('Enter choice\n1 to add entry\n2 to Search meaning of a word\n3 to display synonyms\n4 to print words in alphabetical order\n5 to delete an entry 0 to exit\n'))
    if ch==1:
        AddWord()
    elif ch==2:
        SearchWord()
    elif ch==3:
        DisplayWordsWithSameMeaning()
    elif ch==4:
        Sort()
    elif ch==5:
        RemoveEntry()
    else:
        break
