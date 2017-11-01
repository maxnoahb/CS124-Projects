# Recursive version:
def fib_rec(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fib_iter(n):
	A = [0, 1]
	for i in range(2, 1000):
		A.append(A[i-1] + A[i-2])
	return A[n]




print(fib_iter(3))
print(fib_iter(4))
print(fib_iter(5))
print(fib_iter(9))
print(fib_iter(10))