def find_demlo(s): 
	l = len(s) 
	res = "" 
	for i in range(1,l+1): 
		res = res + str(i) 
	for i in range(l-1,0,-1): 
		res = res + str(i) 
	return res 	