// AUTHOR: WangQiang
// CREATE DATE:   20140526
// LAST UPDATE DATE: 20140528
// EMAIL:  cntqrxj@gmail.com

#include <stdio.h>
#include <stdlib.h>

static void submatrix_init(int *S, int S_row, int S_col, int *T, int T_row, int T_col, int row_start, int col_start) {
	int i, j;
	for (i = 0; i < T_row; i++)
		for (j = 0; j < T_col; j++)
			*(T + (i * T_row + j)) = *(S + (S_row * (row_start - 1) + col_start - 1) + i * S_row + j);
}		

static void to_matrix(int *S, int S_row, int S_col, int *M, int M_row, int M_col, int row_start, int col_start) {
	int i, j;
	for (i = 0; i < S_row; i++)
		for (j = 0; j < S_col; j++)
			 *(M + (M_row * (row_start - 1) + col_start - 1) + i * M_row + j) = *(S + (i * S_row + j));
}		

static void matrix_add(int *A, int *B, int *C, int row, int col) {
	int i, j;

	for (i = 0; i < row; i++)
		for (j = 0; j < col; j++)
			*(C + (i * row) + j) = *(A + (i * row) + j) + *(B + (i * row) + j);
}

void square_matrix_multiply(int *A, int *B, int *C, int n) {
	int half = n / 2;
	int num = half * half;
	
	if (n == 1)
		*C = *A * *B;
	else {
		int *A11 = (int *) calloc(num, sizeof(int));
		int *A12 = (int *) calloc(num, sizeof(int));
		int *A21 = (int *) calloc(num, sizeof(int));
		int *A22 = (int *) calloc(num, sizeof(int));
		int *B11 = (int *) calloc(num, sizeof(int));
		int *B12 = (int *) calloc(num, sizeof(int));
		int *B21 = (int *) calloc(num, sizeof(int));
		int *B22 = (int *) calloc(num, sizeof(int));
		int *C11 = (int *) calloc(num, sizeof(int));
		int *C12 = (int *) calloc(num, sizeof(int));
		int *C21 = (int *) calloc(num, sizeof(int));
		int *C22 = (int *) calloc(num, sizeof(int));
		int *D11 = (int *) calloc(num, sizeof(int));
		int *D12 = (int *) calloc(num, sizeof(int));
		int *D21 = (int *) calloc(num, sizeof(int));
		int *D22 = (int *) calloc(num, sizeof(int));

		submatrix_init(A, n, n, A11, half, half, 1, 1);
		submatrix_init(A, n, n, A12, half, half, 1, half + 1);
		submatrix_init(A, n, n, A21, half, half, half + 1, 1);
		submatrix_init(A, n, n, A22, half, half, half + 1, half + 1);
		submatrix_init(B, n, n, B11, half, half, 1, 1);
		submatrix_init(B, n, n, B12, half, half, 1, half + 1);
		submatrix_init(B, n, n, B21, half, half, half + 1, 1);
		submatrix_init(B, n, n, B22, half, half, half + 1, half + 1);
		square_matrix_multiply(A11, B11, C11, half);
		square_matrix_multiply(A12, B21, D11, half);	
		square_matrix_multiply(A11, B12, C12, half);
		square_matrix_multiply(A12, B22, D12, half);
		square_matrix_multiply(A21, B11, C21, half);
		square_matrix_multiply(A22, B21, D21, half);
		square_matrix_multiply(A21, B12, C22, half);
		square_matrix_multiply(A22, B22, D22, half);
		matrix_add(C11, D11, C11, half, half);	
		matrix_add(C12, D12, C12, half, half);	
		matrix_add(C21, D21, C21, half, half);	
		matrix_add(C22, D22, C22, half, half);	
		to_matrix(C11, half, half, C, n, n, 1, 1); 
		to_matrix(C12, half, half, C, n, n, 1, half + 1); 
		to_matrix(C21, half, half, C, n, n, half + 1, 1); 
		to_matrix(C22, half, half, C, n, n, half + 1, half + 1); 
		free(A11);
        free(A12);
        free(A21);
        free(A22);
        free(B11);
        free(B12);
        free(B21);
        free(B22);
        free(C11);
        free(C12);
        free(C21);
        free(C22);
        free(D11);
        free(D12);
        free(D21);
		free(D22);
	}
	return;
}
