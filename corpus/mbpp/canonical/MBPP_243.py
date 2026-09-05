def sort_on_occurence(lst): 
	dct = {} 
	for i, j in lst: 
		dct.setdefault(i, []).append(j) 
	return ([(i, *dict.fromkeys(j), len(j)) 
				for i, j in dct.items()]) 