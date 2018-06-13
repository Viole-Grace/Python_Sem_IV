def abc(word):
	l= list(word)
	count=0
	print "Word \t | Type\n"
	for item in l:
		s=''.join(sorted(item))
		if s!=item:
			print item," : \tNot abecedarian"
		else:
			print item," : \tAbecedarian"
			count+=1
	print "NO. of abecedarian words : ",count

y=raw_input("Enter string : ").split()
abc(y)