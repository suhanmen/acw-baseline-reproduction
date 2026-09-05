def solution (a, b, n): 
	i = 0
	while i * a <= n: 
		if (n - (i * a)) % b == 0: 
			return ("x = ",i ,", y = ", 
			int((n - (i * a)) / b)) 
			return 0
		i = i + 1
	return ("No solution") 