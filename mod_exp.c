#include <stdio.h>

unsigned long modular_exponentiation(unsigned long a, unsigned long b, unsigned long n) {
	unsigned long c = 0;
	unsigned long d = 1;
	int k = sizeof(unsigned long) * 8 - 1;
	unsigned long mask = 1 << k;
	unsigned long shift = b;
	int i;
	for (i = k; i >= 0; i--) {
		c = 2 * c;
		d = (d * d) % n;
		if ((shift & mask) == mask)
		{
			c = c + 1;
			d = (d * a) % n;
		}
		shift = shift << 1;
	}
	return d;
}

