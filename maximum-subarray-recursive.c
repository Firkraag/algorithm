#include <stdio.h>
#include <limits.h>

struct value {
	int low;
	int high;
	int sum;
};

//FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
//	left-sum = NEGATIVE INFINITE
//	sum = 0
//	for i = mid downto low
//		sum = sum + A[i]
//		if sum > left-sum
//			left-sum = sum
//			max-left = i
//	right-sum = NEGATIVE INFINITE
//	sum = 0
//	for j = mid + 1 to high
//		sum = sum + A[j]
//		if sum > right-sum
//			right-sum = sum
//			max-right = j
//	return(max-left,max-right,left-sum + right-sum)


struct value FIND_MAX_CROSSING_SUBARRAY(int A[], int low, int mid, int high) {
	int left_sum = INT_MIN;
	int right_sum = INT_MIN;
	int max_left, max_right;
	int sum = 0;
	int i;
	struct value cross;
	for(i = mid; i >= low; i--) {
		sum = sum + A[i];
		if (sum >= left_sum) 
		{	left_sum = sum;
 			max_left = i;
		}
	}
	sum = 0;
	for (i = mid + 1; i <= high; i++) {
		sum = sum + A[i];
		if (sum >= right_sum) {
			right_sum = sum;
			max_right = i;
		}
	}
	cross.low = max_left;
	cross.high = max_right;
	cross.sum = left_sum + right_sum;
	return cross;
//	printf("%d, %d, %d\n", max_left, max_right, left_sum + right_sum);
}

//FIND-MAXIMUM-SUBARRAY(A, low, high)
//	if high == low
//		return(low, high, A[low])
//	else mid = floor of (low + high) / 2
//		(left-low, left-high, left-sum) =
//			FIND-MAXIMUM-SUBARRAY(A, low, mid)
//		(right-low, right-high, right-sum) =
//			FIND-MAXIMUM-SUBARRAY(A, mid + 1, high)
//		(cross-low, cross-high, cross-sum) =
//			FIND-MAXIMUM-SUBARRAY(A, low, mid, high)
//		if left-sum >= right-sum and left-sum >= cross-sum
//			return(left-low, left-high, left-sum)
//		elseif right-sum >= left-sum and right-sum >= cross-sum
//			return(right-low, right-high, right-sum)
//		else return(cross-low, cross-high, cross-sum)

struct value FIND_MAXIMUM_SUBARRAY(int A[], int low, int high) {
	struct value left, right, cross;
	int mid;

	if (low == high) {
		left.low = low;
		left.high = high;
		left.sum = A[low];
		return left;
	}
	else {
		mid = (low + high) / 2;
		left = FIND_MAXIMUM_SUBARRAY(A, low, mid);
		cross = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high);
		right = FIND_MAXIMUM_SUBARRAY(A, mid + 1, high);
		if (left.sum >= right.sum && left.sum >= cross.sum)
			return left;
		else if (right.sum >= left.sum && right.sum >= cross.sum)
			return right;
		else
			return cross;
	}
}
int main() {
	//int a[17] = { 13, -3, -25, -20, -3, -16, 23, 18, 20, -7, 12, -5, 22, -15, -4, 7, 0};
	struct value max;	
	int b[6] = {-6, -2, -2, -2, -10, -1};
//
	//max = FIND_MAXIMUM_SUBARRAY(a, 0, 16);
	max = FIND_MAXIMUM_SUBARRAY(b, 0, 5);
	//printf("%d, %d, %d, %d, %d\n", max.low, max.high, max.sum, a[max.low], a[max.high]);
	printf("%d, %d, %d\n", max.low, max.high, max.sum);
	return 0;
}
