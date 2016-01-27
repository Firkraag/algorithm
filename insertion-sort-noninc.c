#include <stdio.h>
//Sort into nonincreasing order
void insertionsort(int s[], int length) {
	int j, i;
	int key;

	for (j = 1; j < length; j++) {
		key = s[j];
		for (i = j - 1; i >= 0 && s[i] < key; i--)
			s[i+1] = s[i];
		s[i+1] = key;
		for (i = 0; i < length; i++)
			printf("%d ", s[i]);
		printf("\n");
	}
}
