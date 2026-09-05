def is_palindrome(n) : 
	divisor = 1
	while (n / divisor >= 10) : 
		divisor *= 10
	while (n != 0) : 
		leading = n // divisor 
		trailing = n % 10
		if (leading != trailing) : 
			return False
		n = (n % divisor) // 10
		divisor = divisor // 100
	return True
def largest_palindrome(A, n) : 
	A.sort() 
	for i in range(n - 1, -1, -1) : 
		if (is_palindrome(A[i])) : 
			return A[i] 
	return -1