//BinSearch(A, first, end, x)
//	while length >= 0
//		inter = (first + end) / 2
//		if x == A[inter]
//			return inter + 1
//		else if x < A[inter]
//			end = inter - 1
//		else
//			first = inter + 1
//		length = end - first
//	return -1
	
int BinSearch(int A[], int first, int end, int x) {
	int length = end - first;
	int inter;
	
	while (length >= 0) {
		inter = (first + end) / 2;
		if (x == A[inter] )
			return inter + 1;
		else if (x < A[inter])
			end = inter - 1;
		else
			first = inter + 1;
		length = end - first;	
	}
	return -1;
}

void main() {
	int A[10] = {0,1,2,3,4,5,6,7,8,9};
	
	printf("%d\n", BinSearch(A, 0, 9, 9));
}	
