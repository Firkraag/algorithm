// This program determines the number of inversions in 
// any permution on n elements using a global variable invs
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

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
static int invs = 0;

static void combine(int B[], int first, int inter, int end)
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
		L[i] = B[first + i];
	for (j = 0; j < len2; j++)
		R[j] = B[inter + j + 1];
	L[len1] = INT_MAX;
	R[len2] = INT_MAX;

	i = 0;
	j = 0;
	for (k = first; k <= end; k++)
	{
		if (L[i] <= R[j])
			B[k] = L[i++]; else { B[k] = R[j++];
			invs = invs + len1 - i;
		}

	}
	free(L);
	free(R);
}

static void divide(int B[], int first, int end)
{
	if (first < end)
	{
		int middle = (first + end) / 2;

	    divide(B, first, middle);
		divide(B, middle + 1, end);
		combine(B, first, middle, end);
	}
}

int inversion(int A[], int first, int end) {
	int i;
	int *B = (int *) calloc(end - first + 1, sizeof(int));

	for (i = first; i <= end; i++)
		B[i] = A[i];
	divide(B, first, end);
	free(B);
	i = invs;
	invs = 0;
	return i;
}
