def sum_three_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:3])