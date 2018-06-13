def initials(name):
	print"Initials : ",
	string=""
	for word in name.split(' '):
		string=string+word[0].upper()
	print string
name=raw_input("Enter Full Name : ")
initials(name)