//This procedure implements Horner's rule for evaluating
//a polynomial
#include <stdio.h>
#include <math.h>

void Horner(int A[], int n, int x)  {
	int sum = 0;
	int i;
	
	for (i = n; i >= 0; i--)
	    sum = A[i] + x * sum;
	printf("%d\n", sum);
}

//void Horner2(int A[], int n, int x)  {
	//int sum = 0;
	//int i;
//	
	//for (i = n; i >= 0; i--)
	    //sum = A[i] * pow(x, i) + sum;
	//printf("%d\n", sum);
//}

int main() {
	int a[10] = {1,2,30,4,5,6,7,8,9,0};
	
	Horner(a, 9, 2);
	//Horner2(a, 9, 2);
	return 0;
}
	
	
	     
	
