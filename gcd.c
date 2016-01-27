#include <stdio.h>

/* gcd: compute the greatest common divisor of m and n;
 	return value: gcd   */
 unsigned gcd(unsigned m, unsigned n) {
	unsigned rem;

	while (n > 0)
	{
		rem = m % n;
		m = n;
		n = rem;
	}
	return m;
}

int main() {
	printf("%u\n", gcd(63 - 1194 + 1387, 1387));
	printf("%u\n", gcd(1273, 1387));
	return 0;
}
