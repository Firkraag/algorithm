//* This program uses insertion sort within merge sort when subproblems
//* become sufficiently small
				// MERGE(A, p, q, r)
	// n1 = q - p + 1
	// n2 = r - q
	// L[1...n1] = A[p...q]
	// R[1...n2] = A[q+1...r]
	// L[n1+1] = ∞
	// R[n2+1] = ∞
	// i = 1
	// j = 1
	// for k = p to r
	// if L[i] <= R[j]
	// A[k] = L[i]
	// i = i + 1
	// else
	// A[k] = R[j]
	// j = j + 1
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

void InsSort(int a[], int n)
{
	int i, j;
	int key;
	for (i = 1; i < n; i++)
	{
		key = a[i];
		for (j = i - 1; j >= 0 && a[j] > key; j--)
		{
			a[j + 1] = a[j];
			a[j] = key;
		}
	}
}

void MERGE(int A[], int first, int inter, int end)
{
	int len1 = inter - first + 1;
	int len2 = end - inter;
	int i;
	int j;
	int k;
	int *L;
	int *R;

	L = (int *)calloc(len1 + 1, sizeof(int));
	R = (int *)calloc(len2 + 1, sizeof(int));
	for (i = 0; i < len1; i++)
		L[i] = A[first + i];
	for (j = 0; j < len2; j++)
		R[j] = A[inter + j + 1];
	L[len1] = INT_MAX;
	R[len2] = INT_MAX;

	i = 0;
	j = 0;
	for (k = first; k <= end; k++)
	{
		if (L[i] <= R[j])
			A[k] = L[i++];
		else
			A[k] = R[j++];
	}
	free(L);
	free(R);
}

void MergeSort(int A[], int n, int length)
{
	int num = n / length;
	int last_length = n - (num - 1) * length;
	int i;

	for (i = 1; i < num; i++)
	{
		InsSort(A + (i - 1) * length, length);
		if (i > 1)
			MERGE(A, 0 , (i - 1) * length - 1, i * length - 1);
	}
	InsSort(A + (i - 1) * length, last_length);
	MERGE(A, 0, (i - 1) * length - 1, n - 1);
}

int main()
{
	int a[77];
	int i;

	for (i = 0; i < 77; i++)
		a[i] = 77 - i;
	MergeSort(a, 77, 9);
	for (i = 0; i < 77; i++)
		printf("%d\t", a[i]);
	printf("\n");
	return 0;
}
