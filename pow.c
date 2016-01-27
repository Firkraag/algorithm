// AUTHOR: WangQiang
// CREATE DATE: 	   
// LAST UPDATE DATE: 20140524
// EMAIL:  cntqrxj@gmail.com

/* pow: comput x^n; return value: x ^ n */
int pow1(int x, unsigned n) {
	int square;

	if (n == 0)
		return 1;
	if (n == 1)
		return x;

	square = x * x;
	if (n == 2)
		return square;
	if (n % 2)
		return pow1(square, n / 2) * x;
	else
		return pow1(square, n / 2);
}

int pow2(int x, unsigned n) {
	int tmp;

	if (n == 0)
		return 1;
	if (n == 1)
		return x;
	if (n == 2)
		return x * x;
	tmp = pow2(x, n / 2);
	if (n % 2) 
		return tmp * tmp * x;
	else
		return tmp * tmp;
}
