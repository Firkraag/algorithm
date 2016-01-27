#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void FengSort(int A[], int first, int end)
{
	int length = end - first + 1;
	int MAX = 100;
	int *B = (int *)calloc(MAX + 1, sizeof(int));
	int i, j;
	int LIMIT = MAX + 1;

	for (i = 1; i <= MAX; i++)
		B[i] = LIMIT;
	for (i = 0; i < length; i++)
		B[A[i]] = A[i];
	j = 0;
	for (i = 1; i <= MAX; i++)
		if (B[i] != LIMIT)
			A[j++] = B[i];
	free(B);
}

int main()
{
	int a[9] = { 3, 41, 52, 31, 31, 57, 9, 31, 100 };
	int b[2]	=	{100, 2};
	// int a[2] = {4,3};
	// int a[3] = {4, 3, 1};
	// Combine(a, 0, 3, 5);
	FengSort(a, 0, 8);
	printf("%d, %d, %d, %d, %d, %d, %d, %d, %d\n", a[0], a[1], a[2], a[3],
		   a[4], a[5], a[6], a[7], a[8]);
     FengSort(b, 0, 1);
     printf("%d,%d\n", b[0], b[1]);
	 exit(0);
} 
