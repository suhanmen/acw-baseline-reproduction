import math
def largest_triangle(a,b): 
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area 