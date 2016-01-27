#include <stdio.h>

void SelectionSort(int *A, int n) {
	int i, j;
	int min, index;
	int tmp;

	for (i = 0; i < n - 1; i++) {
		min = A[i];
		index = i;

		for (j = i + 1; j < n; j++)
			if (A[j] < min) {
				min = A[j];
				index = j;
			}
		tmp = A[i];
		A[i] = A[index];
		A[index] = tmp;
	}
}

int main() {
	int A[6] = {6, 5, 5, 3, 100, 1};
	
	SelectionSort(A, 6);
	printf("%d, %d, %d, %d, %d, %d\n", A[0], A[1], A[2], A[3], A[4], A[5]);
	return 0;
}
