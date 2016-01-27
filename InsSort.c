#include  <stdio.h>

void InsSort(int a[], int n)
{
	int i, j;
	int key;
	for (i = 1; i < n; i++)
	{
		key = a[i];
		for (j = i - 1; j >= 0 && a[j] > key; j--)
		{
			a[j + 1] = a[j];
			a[j] = key;
		}
	}
}

void main()
{
	int a[6] = { 31, 41, 59, 26, 61, 58 };

	InsSort(a, 6);
	printf("%d,%d,%d,%d,%d,%d", a[0], a[1], a[2], a[3], a[4], a[5]);
}