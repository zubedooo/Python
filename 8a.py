def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True   
fin = open('words.txt','w+')
fin.write("abcd qwsa ljkl wd xxx abcd\n dqdas\ndads\ndasd")
fin.close()
fin = open('words.txt','r+')
count = 0
for line in fin:
    for word in line.split():
        if is_abecedarian(word):
            count += 1
print('There are {} abecedarian words.'.format(count))
fin.close()
