phones=dict()
def addentry():
    global phones
    name=input('Enter name of the phone ')
    price=input('Enter price ')
    phones.update({name:price})
def search_by_name(name1):
    global phones
    for key,value in phones.items():
        if name1==key:
            print('Found, its price is ',value)
def search_by_price(name1):
    global phones
    for key,value in phones.items():
        if name1==value:
            print('Found, name of the phone is ',key)
def group_by_price():
    global phones
    pricelist = sorted(phones.values())
    pricelist = list(set(pricelist))   #removes duplicate values
    pricelist.append(None)
    print('Phones grouped by same prices are ')
    while pricelist[0] != None:
        for key,value in phones.items():
            if value == pricelist[0]:
                print(key,end=', ')
        print(' ')
        del(pricelist[0])
def remove_entry():
    global phones
    print('Enter name of phone to delete ')
    name=input();
    try:
        del(phones[name])
        print(phones.keys())
    except:
        print('Entry not found')
def sortdict():
    print(sorted(phones.items(), key = lambda x: x[1])) #sort by price, for sorting by name use x[0]

# DRIVER CODE
while True:
    print('Enter 1 to add entry, 2 to search by name, 3 to search by price,\n'
          '4 to group by price, 5 to sort,6 to delete entry, 0 to exit\n')
    choice=int(input())
    if choice==1:
        addentry()
    elif choice==2:
        name=input('Enter name of the phone ')
        search_by_name(name)
    elif choice==3:
        price = input('Enter name of the phone ')
        search_by_price(price)
    elif choice==4:
        group_by_price()
    elif choice == 5:
        sortdict()
    elif choice==6:
        remove_entry()
    else:
        break

