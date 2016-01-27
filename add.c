#include <stdio.h>

#define N 2
 void submatrix_init(int *S, int S_row, int S_col, int *T, int T_row, int T_col, int row_start, int col_start);

int main() {
	int A[16] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
	int B[4]  = {1, 2, 3, 4};
	int C[4]  = {1, 0, 2, 1};
	int D[4];
	int E[4];
	int i, j;
	
	
	//submatrix_init(A, 4, 4, B, 2, 2, 1, 1);
	//submatrix_init(A, 4, 4, C, 2, 2, 1, 3);
	//submatrix_init(A, 4, 4, D, 2, 2, 3, 1);
	//submatrix_init(A, 4, 4, E, 2, 2, 3, 3);
	//printf("Matrix A:\n");
	//for (i = 0; i < 4; i++) {
		//for (j = 0; j < 4; j++)
			//printf("%d\t", *(A + 4 * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("Matrix B:\n");
	//for (i = 0; i < N; i++) {
		//for (j = 0; j < N; j++)
			//printf("%d\t", *(B + N * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("Matrix C:\n");
	//for (i = 0; i < N; i++) {
		//for (j = 0; j < N; j++)
			//printf("%d\t", *(C + N * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("Matrix D:\n");
	//for (i = 0; i < N; i++) {
		//for (j = 0; j < N; j++)
			//printf("%d\t", *(D + N * i + j));
		//printf("\n");
	//}
	//printf("\n");
	//printf("Matrix E:\n");
	//for (i = 0; i < N; i++) {
		//for (j = 0; j < N; j++)
			//printf("%d\t", *(E + N * i + j));
		//printf("\n");
	//}
	//printf("\n");
	square_matrix_multiply(B, C, E, 2); 
	printf("Matrix E:\n");
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++)
			printf("%d\t", *(E + N * i + j));
		printf("\n");
	}
	printf("\n");
}	
