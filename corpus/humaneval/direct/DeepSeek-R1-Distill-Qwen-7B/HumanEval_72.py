def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w.
    '''
    # Check if the list is a palindrome
    for i in range(len(q) // 2):
        if q[i] != q[-i - 1]:
            return False
    # Check if the sum is less than or equal to the maximum weight
    if sum(q) > w:
        return False
    return True