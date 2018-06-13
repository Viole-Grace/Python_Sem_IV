class triangle():
	sumofangles=0
	def __init__(self,angle1,angle2,angle3):
		global sumofangles
		self.angle1=angle1
		self.angle2=angle2
		self.angle3=angle3
		sumofangles=self.angle1+self.angle3+self.angle2
	noofsides=3
	def checkangles(self):
		global sumofangles
		if sumofangles != 180:
			print "False : ",sumofangles
		else:
			print "True"

angle1=int(raw_input("Enter angle 1 : "))
angle2=int(raw_input("Enter angle 2 : "))
angle3=int(raw_input("Enter angle 3 : "))
obj = triangle(angle1,angle2,angle3)
obj.checkangles()
print"NO. of sides : ", obj.noofsides