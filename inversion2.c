// This program determines the number of inversions in 
// any permution on n elements
// This version no longer uses global variable. It is more 'divide and conquer' than inversion.c
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

static int combine(int B[], int first, int inter, int end)
{
	int len_left = inter - first + 1;
	int len_right = end - inter;
	int i;
	int j;
	int k;
	int *L;
	int *R;
	int invs_cross = 0;

	L = (int *)calloc(len_left + 1, sizeof(int));
	R = (int *)calloc(len_right + 1, sizeof(int));
	for (i = 0; i < len_left; i++)
		L[i] = B[first + i];
	for (j = 0; j < len_right; j++)
		R[j] = B[inter + j + 1];
	L[len_left] = INT_MAX;
	R[len_right] = INT_MAX;

	i = 0;
	j = 0;
	for (k = first; k <= end; k++)
	{
		if (L[i] <= R[j])
			B[k] = L[i++]; 
		else { 
			B[k] = R[j++];
			invs_cross = invs_cross + len_left - i;
		}

	}
	free(L);
	free(R);
	return invs_cross;
}

int divide(int B[], int first, int end)
{
	int invs_left, invs_right, invs_cross;

	if (first < end)
	{
		int middle = (first + end) / 2;

		invs_left = divide(B, first, middle);
		invs_right = divide(B, middle + 1, end);
		invs_cross = combine(B, first, middle, end);
		return invs_left + invs_right + invs_cross;
	}
	return 0;
}

int inversion(int A[], int first, int end) {
	int i;
	int *B = (int *) calloc(end - first + 1, sizeof(int));

	for (i = first; i <= end; i++)
		B[i] = A[i];
	i =  divide(B, first, end);
	free(B);
	return i;
}
