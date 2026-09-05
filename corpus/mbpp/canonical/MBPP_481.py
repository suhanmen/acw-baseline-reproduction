def is_subset_sum(set, n, sum):
	if (sum == 0):
		return True
	if (n == 0):
		return False
	if (set[n - 1] > sum):
		return is_subset_sum(set, n - 1, sum)
	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])