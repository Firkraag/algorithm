/* max_subsequence_sum: compute max subsequence sum of a[n]  
	on-lines algorithms; O(n) */
int max_subsequence_sum(int a[], unsigned n) {
	int this_sum, max_sum, best_i, best_j, i, j;

	i = this_sum = max_sum = 0; best_i = best_j = -1;
	for (j = 0; j < n; j++) {
		this_sum += a[j];
		if (this_sum > max_sum)
		{	/* update max_sum, best_i, best_j */
			max_sum = this_sum;
			best_i = i;
			best_j = j;
		} else if (this_sum < 0) {
			i = j + 1;
			this_sum = 0;
		}
	}
	return max_sum;
}

