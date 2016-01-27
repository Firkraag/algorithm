#include <stdio.h>
#include <limits.h>

struct value {
        int low;
        int high;
        int sum;
};

//An inline solution to find maximum subarray
//FIND_MAXIMUM_SUBARRAY(A, low, high)
//	sum = A[low]
//	left = low
//	right = high
//	max-endpoint-sum = NEGATIVE INFINITE
//	for i = low to high
//		if max-endpoint-sum >= 0
//			max-endpoint-sum = max-endpoint-sum + A[i]
//			max-endpoint-high = i
//		else
//			max-endpoint-sum = A[i]	
//			max-endpoint-low = max-endpoint-high = i
//		if max-endpoint-sum > sum
//			sum = max-endpoint-sum
//			left = max-endpoint-low
//			right = max-endpoint-high
//	return(left, right, sum)			
struct value FIND_MAXIMUM_SUBARRAY(int A[], int low, int high) {
	struct value max_endpoint, max; 
	int i;

	max.sum = A[low];
	max.low = low;
	max.high = high;
	max_endpoint.sum = INT_MIN;

	for (i = low; i <= high; i++) {
		if (max_endpoint.sum >= 0) {
			max_endpoint.sum = max_endpoint.sum + A[i];
			max_endpoint.high = i;
		}
		else {
			max_endpoint.sum = A[i];
			max_endpoint.low = max_endpoint.high = i;
		}
		if (max_endpoint.sum > max.sum) {
			max.sum = max_endpoint.sum;
			max.low = max_endpoint.low;
			max.high = max_endpoint.high;
		}
	}
	return max;
}

int main() {
        int a[17] = { 13, -3, -25, -20, -3, -16, 23, 18, 20, -7, 12, -5, 22, -15, -4, 7, 0};
        struct value max;       

        max = FIND_MAXIMUM_SUBARRAY(a, 0, 16);
        printf("%d, %d, %d, %d, %d\n", max.low, max.high, max.sum, a[max.low], a[max.high]);
		return 0;
}
