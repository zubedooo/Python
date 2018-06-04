def is_abecedarian(word):
    return(word==''.join(sorted(word)))
file = open('words.txt','w+')
file.write(input("Enter some words please: "))
file.close()
with open('words.txt','r+') as file:
    count=0
    for line in file:
        for word in line.split():
            if is_abecedarian(word):
                count+=1
    print("There are",count,"Abecedarian words")
