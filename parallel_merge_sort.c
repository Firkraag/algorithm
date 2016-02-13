#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>

int binary_search(int x, int *T, int p, int r)
{
	int low = p;
	int high = (p < (r + 1) ? (r + 1) : p);
	int mid;

	while (low < high)
	{
		mid = (low + high) / 2;
		if (x <= T[mid])
			high = mid;
		else
			low = mid + 1;
	}
	return high;
}

void swap(int *p1, int *p2)
{
	int tmp = *p1;

	*p1 = *p2;
	*p2 = tmp;
	return;
}

void parallel_merge(int *T, int p1, int r1, int p2, int r2, int *A, int p3)
{
	int q1, q2, q3;
	int n1 = r1 - p1 + 1;
	int n2 = r2 - p2 + 1;

	if (n1 < n2)
	{
		swap(&p1, &p2);
		swap(&r1, &r2);
		swap(&n1, &n2);
	}
	if (n1 == 0)
		return;
	else
	{
		q1 = (p1 + r1) / 2;
		q2 = binary_search(T[q1], T, p2, r2);
		q3 = p3 + (q1 - p1) + (q2 - p2);
		A[q3] = T[q1];
#pragma omp parallel sections shared(T, p1, q1, p2, q2, A, p3, q3)
		{
#pragma omp section
			parallel_merge(T, p1, q1 - 1, p2, q2 - 1, A, p3);
#pragma omp section
			parallel_merge(T, q1 + 1, r1, q2, r2, A, q3 + 1);
		}
		return;
	}
}
void parallel_merge_sort(int *A, int p, int r, int *B, int s)
{
	int n = r - p + 1;

	if (n == 1)
	{
		B[s] = A[p];
		return;
	}
	else
	{
		int *T = (int *) malloc(sizeof(int) * n);
		int q1 = (p + r) / 2;
		int q2 = q1 - p + 1;

		#pragma omp parallel sections shared(A, p, q1, T, r, q2)
		{
#pragma omp section
			parallel_merge_sort(A, p, q1, T, 0);
#pragma omp section
			parallel_merge_sort(A, q1 + 1, r, T, q2);
		}
		parallel_merge(T, 0, q2 - 1, q2, n - 1, B, s);
		free(T);
		return;
	}
}

int main(int argc, char *argv[])
{
	int i;
	int n = atoi(argv[1]);
	int a[n];
	int b[n];

	omp_set_nested(1);
	srand(time(NULL));
	for (i = 0; i < n; i++)
	{
		a[i] = rand();
	}
	for (i = 0; i < n; i++)
		printf("%d\t", a[i]);
	printf("\n\n");
	parallel_merge_sort(a, 0, n - 1, b, 0);
	for (i = 0; i < n; i++)
		printf("%d\t", b[i]);
	return 0;
}
