#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

//Multiply matrix A of size n * n by vector x of length n, return vector y of length n
int *p_mat_vec(int *A, int *x, int n)
{
	int *y = (int *) malloc(sizeof(int) * n);
	int i, j;
#pragma omp parallel shared(A, x, n) private(i, j)
	{
#pragma omp for
		for (i = 0; i < n; i++)
			y[i] = 0;
#pragma omp for
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				y[i] = y[i] + A[i * n + j] * x[j];
	}
	return y;
}

int main(int argc, char *argv[])
{
	int * p_mat_vec(int *A, int *x, int n);
	int i, j, n;
	int *A, *x, *y;
	printf("Please give n: ");
	scanf("%d",&n);
	if ( (A=(int *)malloc(n * n *sizeof(int))) == NULL )
		perror("memory allocation for a");
	if ( (x=(int *)malloc(n*sizeof(int))) == NULL )
		perror("memory allocation for b");
	printf("Initializing matrix A and vector x\n");
	for (j=0; j<n; j++)
		x[j] = j;
	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			A[i*n+j] = i;
	printf("Executing parallel mxv function for n = %d\n",n);
	y = p_mat_vec(A, x, n);
	for (i = 0; i < n; i++)
		printf("%d\t", y[i]);
	free(A);
	free(x);
	free(y);
	return(0);
}
