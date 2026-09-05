def get_Odd_Occurrence(arr, n):
    """
    Finds the element occurring an odd number of times in a list.

    The logic uses the XOR bitwise operator. XORing a number with itself 
    results in 0, and XORing a number with 0 results in the number itself.
    Therefore, all numbers appearing an even number of times cancel out, 
    leaving only the number that appears an odd number of times.
    """
    result = 0
    for num in arr:
        result ^= num
    return result