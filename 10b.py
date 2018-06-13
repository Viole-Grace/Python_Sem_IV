try :
	print(1+"abc")
except TypeError:
	print ("Type error")
try :
	L=[1,2,3]
	print (L[4])
except IndexError:
	print ("Index error")
