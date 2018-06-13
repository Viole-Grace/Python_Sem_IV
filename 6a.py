print " STARTING INPUT"
s="quit"
l=[]
y=raw_input()
while y != s:
	l.append(y)
	y=raw_input()
print " INPUT HAS ENDED"
print " Given input : ",l
limit = len(l)
print "Reversed output : \n"
for i in range(0,limit):
	print l[limit-i-1],
