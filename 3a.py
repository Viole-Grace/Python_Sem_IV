phones=dict()
def addentry():
    global phones
    name=raw_input("Enter name of the phone:")
    price=raw_input("Enter price:")
    phones.update({name:price})
def namesearch(name1):
    global phones
    for key,value in phones.items():
        if name1==key:
            print "Found, its price is ",value
def pricesearch(price):
    global phones
    searchlist=[k for k,v in phones.items() if v == price]
    print searchlist[0]
def pricegroup():
    global phones
    pricelist = list(set(sorted(phones.values())))   #sorts and removes removes duplicate values
    print "Phones grouped by same prices are :"
    for i in range(len(pricelist)):
	all_keys=pricelist[i]
	print "Price : ",all_keys,"; Group : ",[k for k,v in phones.items() if v == all_keys]
def remove_entry():
    global phones
    print "Enter name of phone to delete :" 
    name=raw_input();
    try:
        del(phones[name])
        print "Updated Dict : \n",phones.keys()
    except:
        print "Entry not found"
def sortdict():
    print sorted(phones.items(),key=lambda x : x[1]) #sort by price, for sorting by name use x[0]
while True:
    print "MENU : \n1. Add Entry \n2. Search by name \n3. Search by price \n4. Group by price \n5. Sort \n6. Delete Entry \n7. Exit \nEnter your choice :"
    choice=int(input())
    if choice==1:
        addentry()
    elif choice==2:
        name=raw_input('Enter name of the phone: ')
        namesearch(name)
    elif choice==3:
        price = (raw_input('Enter price of the phone: '))
        pricesearch(price)
    elif choice==4:
        pricegroup()
    elif choice == 5:
        sortdict()
    elif choice==6:
        remove_entry()
    else:
        break
