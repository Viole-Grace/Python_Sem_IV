s = raw_input("Enter a string : ")
def vowelcount(s):
	counta,counte,counti,countu,counto=0,0,0,0,0
	for i in range(len(s)):
		if s[i]=='a':
			counta+=1
		if s[i]=='e':
			counte+=1
		if s[i]=='i':
			counti+=1
		if s[i]=='o':
			counto+=1
		if s[i]=='u':
			countu+=1
	print " No. of occurrances : \n a : ",counta,"\n e : ",counte,"\n i : ",counti,"\n o : ",counto,"\n u : ",countu
vowelcount(s)
#print "No. of vowels in the given string is : ",count