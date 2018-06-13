dictionary = dict()
def Add():
    global dictionary
    word = raw_input("Enter word : ")
    meaning = raw_input("Enter its meaning : ")
    dictionary[word] = meaning
def Search():
    global dictionary
    search = raw_input("Enter Word to search : ")
    for word,meaning in dictionary.items():
        if word==search:
            print(meaning)
def SameMeaning():
    search = raw_input("Enter meaning : " )
    for word,meaning in dictionary.items():
        if search == meaning:
            print word,
    print "\n"
def Remove():
    search = raw_input("Enter word to delete : ")
    if dictionary.get(search,None) != None:
        del(dictionary[search])
    else:
        print "Word not found "
def Sort():
    print "\nWords in a sorted list are\n",sorted(dictionary,key = lambda x: x[0])
while True:
    choice = int(raw_input("Enter your choice : \n1. Add entry\n2. Search meaning of a word\n3. Display synonyms\n4. Print Lexicographically\n5. Delete an entry \n6. Exit\n"))
    if choice==1:
        Add()
    elif choice==2:
        Search()
    elif choice==3:
        SameMeaning()
    elif choice==4:
        Sort()
    elif choice==5:
        Remove()
    else:
        break