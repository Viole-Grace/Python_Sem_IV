def rotleft():
	a = []
	n=int(input("Enter no. of elements in array : "))
	for i in range(n):
		x=int(input("Enter element : "))
		a.insert(i,x)
	print("Original Array : ")
	print a
	print("After rotation : ")
	y=a.pop(0);a.append(y);
	print a
rotleft()
