class MarksNotEligibleError(Exception):
	pass
class NotAValidIntegerError(Exception):
	pass
try:
	m1,m2,m3=(raw_input("Enter marks for 3 subjects : ").split())
	if m1>50 or m2>50 or m3>50 or m1<0 or m2<0 or m3<0:
		raise NotAValidIntegerError
	if m1<20 or m2<20 or m3<20:
		raise MarksNotEligibleError
except MarksNotEligibleError:
	print(" NOT ELIGIBLE FOR SEE")
except NotAValidIntegerError:
	print(" INVALID MARKS")