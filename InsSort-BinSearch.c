#include  <stdio.h>

void swap(int *a, int *b)
{
	int tmp = *a;

	*a = *b;
	*b = tmp;
}
//Determine where x should be placed in array A
int BinSearch(int A[], int first, int end, int x)
{
	int length = end - first;
	int inter;

	while (length >= 0)
	{
		inter = (first + end) / 2;
		if (x == A[inter])
			return inter;
		else if (x < A[inter])
			end = inter - 1;
		else
			first = inter + 1;
		length = end - first;
	}
//	printf("%d, %d\n", first, end);
	return first;
}

void InsSort(int a[], int n)
{
	int i, j;
	int pos;

	 for (i = 1; i < n; i++)
	{
		pos = BinSearch(a, 0, i - 1, a[i]);
   		for (j = i; j > pos; j--)
			swap(a + j, a + j - 1);
	}
}

int main()
{
	int a[7] = { 31, 101, 59, 26, 0, 61, 58 };

	InsSort(a, 7);
	printf("%d,%d,%d,%d,%d,%d,%d\n", a[0], a[1], a[2], a[3], a[4], a[5], a[6]);
	return 0;
}
