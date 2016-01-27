void swap(int *x, int *y) {
	int temp;

	temp = *x;
	*x = *y;
	*y = temp;
}

/* Compute Fibonacci number fib(n); fib(0) = 1, fib(1); fib(n) = fib(n-1) + fib(n-2); return fib(n) of int type */

int fib(int n) {
	int fib1 = 1, fib2 = 1;
	int i;

	for (i = 2; i <= n; i++) {
		fib1 = fib1 + fib2;
		swap(&fib1, &fib2);
	}
	return fib2;
	
}

