import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    """
    # Extract the numerical values from the string using regex
    numbers = re.findall(r'\d+', s)
    apples = int(numbers[0])
    oranges = int(numbers[1])
    # Calculate the number of mango fruits
    return n - apples - oranges