#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int p_fib(int n)
{
	int x, y;

	printf("%d\n", omp_get_nested());
	if (n <= 1)
		return n;
	else
	{
//The values of private data are undefined upon entry to and exit from the specific construct
//So x and y should be declared shared
#pragma omp parallel sections  shared(n, x, y)
		{
#pragma omp section
				x = p_fib(n - 1);
#pragma omp section
				y = p_fib(n - 2);
		}
		return x + y;
	}
}

int main(int argc, char *argv[])
{
	printf("%d\n", omp_get_nested());
	omp_set_nested(1);
	printf("%d\n", p_fib(atoi(argv[1])));
	return 0;
}

