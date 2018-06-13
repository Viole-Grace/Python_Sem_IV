import Sample
#word=raw_input("Enter a string : ")
while True:
	ch=int(raw_input("Enter your choice : \n1.Push Elements into Stack\n2.Pop Elements From the Stack\n3.Get value of Top\n"))
	if ch==1:
		word=raw_input("Enter a string : ")
		Sample.main.input(word)
	elif ch==2:
		Sample.main.remove(word)
	elif ch==3:
		Sample.stack.getTop()
	else:
		break