def right_rotate(arr, n, out_of_place, cur):
	temp = arr[cur]
	for i in range(cur, out_of_place, -1):
		arr[i] = arr[i - 1]
	arr[out_of_place] = temp
	return arr
def re_arrange(arr, n):
	out_of_place = -1
	for index in range(n):
		if (out_of_place >= 0):
			if ((arr[index] >= 0 and arr[out_of_place] < 0) or
			(arr[index] < 0 and arr[out_of_place] >= 0)):
				arr = right_rotate(arr, n, out_of_place, index)
				if (index-out_of_place > 2):
					out_of_place += 2
				else:
					out_of_place = - 1
		if (out_of_place == -1):
			if ((arr[index] >= 0 and index % 2 == 0) or
			 (arr[index] < 0 and index % 2 == 1)):
				out_of_place = index
	return arr