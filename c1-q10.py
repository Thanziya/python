print ("-----Enter two positive integer numbers-----")
p = int (input ())
q = int (input ())

while p != q:
	if p > q:
		p -= q
	else:
		q -= p

print ("\nThe GCD of numbers is: ", p)
