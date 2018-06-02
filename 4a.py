name = raw_input("Enter Name")
def Initials(n):
    initials= ''.join([s[:1].upper() for s in n.split(' ')])
    return initials
print (Initials(name))
