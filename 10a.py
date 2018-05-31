from Mystring import PalAndVowCount
inp = input("Enter String: ")
opt = int(input("\nSelect:\n(1)Palindrome Check\n(2)Count Vowels\n "))

if opt == 1:
    PalAndVowCount.palindrome(inp)
elif opt == 2:
    PalAndVowCount.vowcount(inp)

#For the code to work create a package
#right click on your program in the yellow column on the left
#New -- Python Package
#Write PalAndVowCount.py in that