#include <stdio.h>
//INSERTION-SORT(A)
	//for j = 2 to A.length
		//key = A[j]
		////Insert A[j] into the sorted sequence A[1..j - 1].
		//i = j - 1
		//while i > 0 and A[i] > key
			//A[i + 1] = A[i]
			//i = i - 1
		//A[i + 1] = key

//Sort into nondecreasing order
void insertionsort(int s[], int length) {
	int j, i;
	int key;

	for (j = 1; j < length; j++) {
		key = s[j];
		for (i = j - 1; i >= 0 && s[i] > key; i--)
			s[i+1] = s[i];
		s[i+1] = key;
//		for (i = 0; i < length; i++)
//			printf("%d ", s[i]);
//		printf("\n");
	}
}
