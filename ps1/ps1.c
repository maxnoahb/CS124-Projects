#include <stdio.h>
#include <time.h>

// recursive implementation
int fib_rec(int n)
{
	if (n <= 1)
    	return n;
	return (fib_rec(n-1) + fib_rec(n-2)) % 65536;
}


// iterative implementation
int fib_iter(int n)
{
	// initialize array to hold Fibonacci sequence 
	int A[n];
	int i;

	// set up initial Fib values
	A[0] = 0;
	A[1] = 1;

	// iteratively append new values of sequence to array
	for (i = 2; i <= n; i++) {
		A[i] = (A[i-1] + A[i-2]) % 65536;
	}

	// return the nth Fib number
	return A[n];
}

// helper function to multiply two matrices
void mult(int B[2][2], int C[2][2])
{
	// basic implementation of matrix multiplication, storing the four numbers in
	// the matrix in integers
	unsigned int a = (B[0][0]*C[0][0] + B[0][1]*C[0][1]) % 65536;
	unsigned int b = (B[0][0]*C[0][1] + B[0][1]*C[1][1]) % 65536;
	unsigned int c = (B[1][0]*C[0][0] + B[1][1]*C[1][0]) % 65536;
	unsigned int d = (B[1][0]*C[0][1] + B[1][1]*C[1][1]) % 65536;

	// update matrix B with the multiplied numbers
	B[0][0] = a;
  	B[0][1] = b;
  	B[1][0] = c;
  	B[1][1] = d;
}

// helper function to raise a matrix to power n
void power(int B[2][2], int n) 
{
	// initialize "reference" matrix from algorithm to multiply later
	int C[2][2] = {{1,1}, {1,0}};

	if (n == 0 || n == 1) {
		return;
	}

	// implement repeated squaring——raise matrix to the n/2 power and then square it
	power(B, n/2);
	mult(B, B);

	// handle the case of an odd exponent——multiply by the reference matrix to
	// adjust the exponent to be even
	if (n % 2 != 0) {
		mult(B, C);
	}
}

// function that returns the nth Fib number with matrix method
int fib_mtrx(int n)
{
	// initialize matrix from the given algorithm
	int B[2][2] = {{1,1}, {1,0}};

	// raise the matrix to the (n-1) power, then return the nth Fib number in the
	// top left corner of the matrix
	power(B, n-1);
	return B[0][0];
}

// main function to call Fib functions and check
int main()
{
	int n = 30;

	// timing function found on StackExchange
	clock_t begin1 = clock();
	int a = fib_rec(n);
	clock_t end1 = clock();
	double time_spent_rec = (double)(end1 - begin1) / CLOCKS_PER_SEC;

	clock_t begin2 = clock();
	int b = fib_iter(n);
	clock_t end2 = clock();
	double time_spent_iter = (double)(end2 - begin2) / CLOCKS_PER_SEC;

	clock_t begin3 = clock();
	int c = fib_mtrx(n);
	clock_t end3 = clock();
	double time_spent_mtrx = (double)(end3 - begin3) / CLOCKS_PER_SEC;
	
	printf("%d, %f seconds \n", a, time_spent_rec);
	printf("%d, %f seconds \n", b, time_spent_iter);
	printf("%d, %f seconds \n", c, time_spent_mtrx);
}