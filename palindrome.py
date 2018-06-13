def palin(word):
	s=""
	for i in range(len(word)):
		s=s+word[len(word)-i-1]
	if s==word:
		print word, " is a Palindrome"
	else:
		print word," isnt a palindrome"

