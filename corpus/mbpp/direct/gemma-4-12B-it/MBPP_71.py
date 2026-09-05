def comb_sort(arr):
    """
    Sorts a list of elements using the Comb Sort algorithm.
    Comb sort improves on bubble sort by using a gap larger than 1 
    to eliminate "turtles" (small values at the end of the list).
    """
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        # Update the gap
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        sorted_flag = True

        # Compare elements with the current gap
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False

    return arr