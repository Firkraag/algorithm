// AUTHOR: WangQiang
// DATE:   20140527
// LAST UPDATE DATE: 20140527
// EMAIL:  cntqrxj@gmail.com

#include <stdio.h>

#define RANK 50

void square_matrix_multiply(int a[][RANK], int b[][RANK], int c[][RANK]) {
	int i, j, k;

	for (i = 0; i < RANK; i++)
		for (j = 0; j < RANK; j++) {
			c[i][j] = 0;
			for (k = 0; k < RANK; k++)
				c[i][j] = c[i][j] + a[i][k] * b[k][j];
		}
}
