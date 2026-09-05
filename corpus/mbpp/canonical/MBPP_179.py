def is_num_keith(x): 
	terms = [] 
	temp = x 
	n = 0 
	while (temp > 0): 
		terms.append(temp % 10) 
		temp = int(temp / 10) 
		n+=1 
	terms.reverse() 
	next_term = 0 
	i = n 
	while (next_term < x): 
		next_term = 0 
		for j in range(1,n+1): 
			next_term += terms[i - j] 
		terms.append(next_term) 
		i+=1 
	return (next_term == x) 