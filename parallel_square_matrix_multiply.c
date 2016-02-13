#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int *parallel_square_matrix_multiply(int *A, int *B, int n)
{
	int *C = (int *) malloc(sizeof(int) * n * n);
	int i, j, k;

#pragma omp parallel  for shared(A, B, C, n) private(i, j, k)
		for (i = 0; i < n; i++)
			//If a thread in a team executing a parallel region encounters another parallel con-
			//struct, it creates a new team and becomes the master of that new team.
			//So the parallel construct is needed, insted of work-sharing region 
#pragma omp parallel for shared(i)
			for (j = 0; j < n; j++)
			{
				printf("%d\n", i);
				C[i * n + j] = 0;
				for (k = 0; k < n; k++)
					C[i * n + j] = C[i * n + j] + A[i * n + k] * B[k * n + j];
			}
	return C;
}

int main(int argc, char *argv[])
{
	int i, j, n;
	int *A, *B, *C;
	printf("Please give n: ");
	scanf("%d",&n);
	if ( (A=(int *)malloc(n * n *sizeof(int))) == NULL )
		perror("memory allocation for matrix A");
	if ( (B=(int *)malloc(n * n *sizeof(int))) == NULL )
		perror("memory allocation for matrix B");
	printf("Initializing matrix A and matrix B\n");
	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
		{
			A[i*n+j] = i;
			B[i*n+j] = i;
		}
	printf("Executing parallel mxv function for n = %d\n",n);
	C = parallel_square_matrix_multiply(A, B, n);
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
//printf("C[%d,%d] = %d%c", i, j, C[i * n + j], j == n - 1 ? '\n' : '\t');
		printf("%d%c", C[i * n + j], j == n - 1 ? '\n' : '\t');
	free(A);
	free(B);
	free(C);
	return(0);
}
