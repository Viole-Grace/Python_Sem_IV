stack = []
top = -1
def getTop():
	global top
	print top
def push(i):
	global top
	stack.append(i) ; top+=1
def pop(i):
	global top
	if top!=-1:
		print stack[top]
		top=top-1
	else:
		print "The Stack is Empty!"
