#include <stdio.h>
// recursive version of insertion sort

void swap(int *a, int *b)
{
	int tmp = *a;

	*a = *b;
	*b = tmp;
}

void Insert(int A[], int n)
{
	int i;

	for (i = n - 1; i >= 0; i--)
		if (A[i] > A[i + 1])
			swap(A + i, A + i + 1);
		else
			return;
}

void InsSort(int A[], int n)
{
	if (n > 1)
	{
		InsSort(A, n - 1);
		Insert(A, n);
	}
	else if (n == 1)
	{
		if (A[0] > A[1])
			swap(A, A + 1);
		return;
	}
	else if (n == 0)
		return;
}

int main()
{
	int a[8] = { 8, 8, 3, 65, 500, 3, -1, 3 };

	InsSort(a, 7);
	printf("%d,%d,%d,%d,%d,%d,%d, %d\n", a[0], a[1], a[2], a[3], a[4], a[5],
		   a[6], a[7]);
	return 0;
}
