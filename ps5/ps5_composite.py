import sys
import math
import random

def repeated_square(n,p):
	if p == 0:
		return 1
	if p == 1:
		return n
	if p % 2 == 1:
		return n * repeated_square(n*n, (p - 1)/2)
	else:
		return repeated_square(n*n, p/2)

def composite(n,a):
	is_composite = False

	if n == 2 or n % 2 == 0:
		is_composite = True

	t = 0
	u = n - 1
	while (u % 2) == 0:
		t += 1
		u //= 2

	x = repeated_square(a, u) % n
	
	for i in range(t):
		if x != 1 and x != n - 1:
			is_composite = True

		x = repeated_square(x, 2) % n

		if x == n - 1:
			is_composite = False
			break

	if is_composite == False:
		print "PRIME"
	else:
		print "COMPOSITE"

print composite(294409, 2)
print composite(636127, 2)