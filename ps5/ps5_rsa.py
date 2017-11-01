import sys
import math
import binascii

def repeated_square(n,p,x):
	if p == 0:
		return 1
	elif p == 1:
		return n % x
	elif p % 2 == 1:
		r = repeated_square(n, (p - 1) / 2, x)
		return (r * r * n) % x
	else:
		r = repeated_square(n, p / 2, x)
		return (r * r) % x

def encode():
	s = "Give me an A"
	n = 46947848749720430529628739081
	e = 37267486263679235062064536973

	# taken from http://stackoverflow.com/questions/18815820/convert-string-to-binary-in-python
	s_binary = '010001110110100101110110011001010010000001101101011001010010000001100001011011100010000001000001'
	s_decimal = int(s_binary, 2)


	c = repeated_square(s_decimal, e, n)
	print c

encode()

