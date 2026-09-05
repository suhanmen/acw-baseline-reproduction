def check_Triangle(x1,y1,x2,y2,x3,y3): 
    a = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))   
    if a == 0: 
        return ('No') 
    else: 
        return ('Yes') 