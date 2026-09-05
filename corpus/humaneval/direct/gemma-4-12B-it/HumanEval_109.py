def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.

    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:

    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.

    """
    if not arr:
        return True

    n = len(arr)
    if n <= 2:
        # Any array of size 1 or 2 that is "sorted" can be shifted
        # but the problem asks if it *can* be sorted. 
        # For size 1, it's always sorted. For size 2, if it's [2, 1], 
        # one right shift makes it [1, 2].
        # However, the logic below handles n >= 1 correctly.
        pass

    # A cyclic shift of a sorted array is "almost" sorted.
    # Specifically, there should be at most one position i where arr[i] > arr[i+1].
    # If there is such a position, the element at the end (arr[n-1]) must be 
    # smaller than the element at the start (arr[0]) to allow a cyclic shift 
    # to fix it.

    count_drops = 0
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            count_drops += 1

    if count_drops == 0:
        return True

    if count_drops == 1:
        # The only drop is between some arr[i] and arr[i+1].
        # For it to be a valid cyclic shift of a sorted array,
        # the last element must be smaller than the first element.
        return arr[n-1] < arr[0]

    return False