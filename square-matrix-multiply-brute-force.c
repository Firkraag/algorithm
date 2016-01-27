// AUTHOR: WangQiang
// DATE:   20140524
// LAST UPDATE DATE: 20140524
// EMAIL:  cntqrxj@gmail.com

#include <stdio.h>

//void square_matrix_multiply(int a[][2], int b[][2], int c[][2]) {
	//int i, j, k;
//
	//for (i = 0; i < 2; i++)
		//for (j = 0; j < 2; j++) {
			//c[i][j] = 0;
			//for (k = 0; k < 2; k++)
				//c[i][j] = c[i][j] + a[i][k] * b[k][j];
		//}
//}

void square_matrix_multiply(int *a, int *b, int *c, int n) {
	int i, j, k;

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			*(c + i * n + j) = 0;
			for (k = 0; k < n; k++)
				*(c + i * n + j) = *(c + i * n + j) + *(a + i * n + k) * *(b + k * n + j);
		}
}

int main() {
	//int d[4] = {1, 3, 7, 5};
	//int e[4] = {6, 8, 4, 2};
	//int f[4];
	//int A[16] = {-1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1};
	int A[16] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
	int B[16], C[16];
	int i, j;
//
	//square_matrix_multiply(d, e, f, 2);
	//printf("Matrix d:\n");
	//for (i = 0; i < 2; i++) {
		//for (j = 0; j < 2; j++)
			//printf("%d\t", *(d + 2 * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("Matrix e:\n");
	//for (i = 0; i < 2; i++) {
		//for (j = 0; j < 2; j++)
			//printf("%d\t", *(e + 2 * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("The result of matrix multiply d * e:\n");
	//for (i = 0; i < 2; i++) {
		//for (j = 0; j < 2; j++)
			//printf("%d\t", *(f + 2 * i + j));
		//printf("\n");
	//}
	square_matrix_multiply(A, A, B, 4);
	//square_matrix_multiply(A, B, C, 4);
	//square_matrix_multiply(C, C, B, 4);
	//printf("Matrix A:\n");
	//for (i = 0; i < 4; i++) {
		//for (j = 0; j < 4; j++)
			//printf("%d\t", *(A + 4 * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("The result is:\n");
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++)
			printf("%d\t", *(B + 4 * i + j));
		printf("\n");
	}
	return 0;
}
