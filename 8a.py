def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True
    
fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print('There are {} abecedarian words.'.format(count))