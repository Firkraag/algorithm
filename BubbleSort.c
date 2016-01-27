//BubbleSort(A)
//for i = 1 to A.length - 1
//	for j = A.length downto i + 1
//		if A[j] < A[j - 1]
//			swap(A[j], A[j - 1])

#include <stdio.h>

void BubbleSort(int A[], int n) {
	int i, j;
	
	for (i = 0; i < n - 1; i++)
		for (j = n - 1; j > i; j--)
			if (A[j] < A[j - 1]) {
				int tmp = A[j];

				A[j] = A[j - 1];
				A[j - 1] = tmp;
			}
}

int main() {
	int a[1000];
	int i;
	
	for (i = 0; i < 1000; i++)
		a[i] = 1000 - i;
	BubbleSort(a, 1000);
	for (i = 0; i < 1000; i++)
		printf("%d\t", a[i]);
	printf("\n");
	return 0;
}
