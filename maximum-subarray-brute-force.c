#include <stdio.h>
#include <limits.h>

struct value {
        int low;
        int high;
        int sum;
};

//A brute-force solution to find maximum subarray: just try every possible pair
struct value FIND_MAXIMUM_SUBARRAY(int A[], int low, int high) {
	int i, j;
	int left, right;
	int sum;
	int max_sum = INT_MIN;
	struct value max;

	for (i = low; i <= high; i++) {
		sum = 0;
		for (j = i; j <= high; j++) {
			sum = sum + A[j];
			if (sum >= max_sum) {
				left = i;
				right = j;
				max_sum = sum;
			}
		}
	}
	max.low = left;
	max.high = right;
	max.sum = max_sum;
	return max;
}

int main() {
    int a[17] = { 13, -3, -25, 20, -3, -16, 23, 18, 20, -7, 12, -5, -22, -15, -4, 7, 0};
    struct value max;
	int b[17] = {100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97};
	int c[16];
	int d[6] = {-6, -100, -8, -2, -5, -1};
	int i;

	for (i = 0; i < 16; i++)
		c[i] = b[i + 1] - b[i];
    max = FIND_MAXIMUM_SUBARRAY(a, 0, 16);
    printf("%d, %d, %d, %d, %d\n", max.low, max.high, max.sum, a[max.low], a[max.high]);
	max = FIND_MAXIMUM_SUBARRAY(c, 0, 15);
    printf("%d, %d, %d, %d, %d, %d, %d\n", max.low, max.high, max.sum, a[max.low], a[max.high], b[max.low], b[max.high + 1]);
	max = FIND_MAXIMUM_SUBARRAY(d, 0, 5);
    printf("%d, %d, %d\n", max.low, max.high, max.sum);
	return 0;
}
