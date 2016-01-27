#include <stdio.h>

void BinaryAdd(int a[], int b[], int n,int c[]) {
		int promote = 0;
		int i;
		int result;
		
		for (i = n - 1; i >= 0; i--) {
			result = a[i] + b[i] + promote;
			if (result >= 2) {
				result = result - 2;
				promote = 1;
			}
			else
				promote = 0;
			c[i + 1] = result;
		}
		c[0] = promote;
}

int main() {
	int a[4] = {1,0,1,1};
	int b[4] = {1,1,1,1};
	int c[5];
	
	BinaryAdd(a, b, 4, c);
	printf("%d%d%d%d + %d%d%d%d = %d%d%d%d%d\n", a[0], a[1], a[2], a[3], b[0], b[1], b[2], b[3], c[0], c[1], c[2], c[3], c[4]);
	return 0;
}
