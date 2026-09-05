def modular_inverse(arr, N, P):
	current_element = 0
	for i in range(0, N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = current_element + 1
	return current_element