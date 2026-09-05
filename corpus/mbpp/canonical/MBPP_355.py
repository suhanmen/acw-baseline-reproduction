def count_Rectangles(radius):  
    rectangles = 0 
    diameter = 2 * radius 
    diameterSquare = diameter * diameter 
    for a in range(1, 2 * radius):  
        for b in range(1, 2 * radius): 
            diagnalLengthSquare = (a * a +  b * b)  
            if (diagnalLengthSquare <= diameterSquare) : 
                rectangles += 1
    return rectangles 