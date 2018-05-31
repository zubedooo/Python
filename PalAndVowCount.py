def palindrome(string):
    print(string==string[::-1])
def vowcount(line):
    vow = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for word in line:
        for char in word:
            if vow.get(char, None) != None:  # second parameter of get is the default value to return if not found
                vow[char] = str(int(vow[char]) + 1)
    print(vow)