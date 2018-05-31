vow = {'a':0,'e':0,'i':0,'o':0,'u':0}
def vowcount(line):
    global vow
    for word in line:
        for char in word:
            if vow.get(char,None)!= None:
                vow[char]=str(int(vow[char])+1)
string=input("Enter a string: ")
vowcount(string)
print(vow)
