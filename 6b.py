class circle():
	def __init__(self,radius):
		self.radius=radius
	def setrad(self,radius):
		if int(radius)<0:
			raise RuntimeError(" Negetive radius is invalid")
		elif int(radius)==0:
			raise RuntimeError(" Zero radius is invalid")
		else:
			self.radius = radius
	def area(self):
		if self.radius>0:
			print "area : ",self.radius**2*3.141596
		else:
			raise RuntimeError("Negetive radius!")
try:
	n=int(raw_input("ENTER RADIUS : "))
except:
	print "Invalid radius",RuntimeError(" no characters allowed, input is of type int")
else:
	try:
		obj=circle(n)
		obj.area()
	except RuntimeError as ex:
		print "Invalid radius again : ",ex
class Aamir(Exception):
	pass
