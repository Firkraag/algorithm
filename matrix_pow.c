// AUTHOR: WangQiang
// DATE:   20140524
// LAST UPDATE DATE: 20140525
// EMAIL:  cntqrxj@gmail.com

#include <stdio.h>
#include <stdlib.h>

void matrix_exp(int *A, int *B, int n, int pow) {
	int length = n * n;
	int *C;
	int i;
	void square_matrix_multiply(int *, int *, int *, int);

	if (pow == 1) {
		for (i = 0; i < length; i++)
			B[i] = A[i];
		return;
	}
	C = calloc(length, sizeof(int));
	matrix_exp(A, C, n, pow / 2);
	square_matrix_multiply(C, C, B, n);
	if (pow % 2) {
		for (i = 0; i < length; i++)
			C[i] = B[i];
		square_matrix_multiply(C, A, B, n);
	}
	free(C);
	return;
}
