def remove_Char(s,c) :  
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s) 