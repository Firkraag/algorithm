#include <stdio.h>
#include <stdlib.h>

//A version of merge procedure that stops once either array L or R has had  //all its elements copied back to A
void Combine(int A[], int first, int inter, int end) {
	int len1 = inter - first + 1;
	int len2 = end - inter; 
	int i;
	int j;
	int k;
	int *L;
	int *R;

	L = (int *) calloc(len1, sizeof(int));
	R = (int *) calloc(len2, sizeof(int));
	for (i = 0; i < len1; i++)
		L[i] = A[first + i];
	for (j = 0; j < len2; j++)
		R[j] = A[inter + j + 1];

	i = 0;
	j = 0;
	k = first;
	while (i < len1 && j < len2)
		if (L[i] <= R[j]) 
			A[k++] = L[i++];
		else
			A[k++] = R[j++];
	if (i == len1)
		while (j < len2)
			A[k++] = R[j++];
	else if (j = len2)
		while (i < len1)
			A[k++] = L[i++];
	free(L);
	free(R);
}

void MergeSort(int A[], int first, int end) {
	int middle = (first + end) / 2;
	
	if (end  == first)
		return;
	MergeSort(A, first, middle);
	MergeSort(A, middle + 1, end);
	Combine(A, first, middle, end);
	return;
}
	
void main() {
	int a[8] = {1,3,4,5,2,6,0,10};
	MergeSort(a, 0, 7);
	printf("%d, %d, %d, %d, %d, %d, %d, %d\n", a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]);
}	
